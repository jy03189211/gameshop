import json, uuid
from hashlib import md5
from django.core.signing import Signer
from gameshop.forms.payment import PaymentForm
from gameshop.models import Game, Order, PaymentStub, Purchase, User
from gameshop.storeutils.cart import cart as cart_utils
from gameshop import settings


def prepare_payment_form(request):
    """Prepares a new payment based on the current cart."""

    cart = request.session.get('cart', [])

    # cart not empty
    if len(cart) > 0:
        # get a new payment id
        pid = uuid.uuid4()
        pid = str(pid)
        amount = cart_utils.get_cart_total(request)

        # seller id and secret key defined in settings
        checksumstr = "pid={}&sid={}&amount={}&token={}".format(
            pid, settings.SELLER_ID, amount, settings.SELLER_SECRET_KEY)

        md5_hash = md5(checksumstr.encode("ascii"))
        checksum = md5_hash.hexdigest()

        # full absolute URL
        base_url = request.META['wsgi.url_scheme'] + '://' \
                    + request.META['HTTP_HOST'] + '/'

        initial_form_data = {
            'pid': pid,
            'sid': settings.SELLER_ID,
            'amount': amount,
            'checksum': checksum,
            'success_url': base_url + settings.PAYMENT_SUCCESS_URL,
            'cancel_url': base_url + settings.PAYMENT_CANCEL_URL,
            'error_url': base_url + settings.PAYMENT_ERROR_URL,
        }

        # if the amount is zero, the payment service will be bypassed and
        # the request can be reduced
        if amount == 0:
            initial_form_data['success_url'] = ''
            initial_form_data['cancel_url'] = ''
            initial_form_data['error_url'] = ''

        payment_form = PaymentForm(initial_form_data)

        # store payment stub in the db for success handling
        # allow anonymous if no logged in user
        user = None
        if request.user.is_authenticated:
            user = request.user

        stub = PaymentStub(
            user=user,
            pid=pid,
            cart_str=json.dumps(cart)
        )
        stub.save()

        return payment_form

    return None


def handle_payment_success(request):
    """Handles game ownership and purchase history after a successful payment"""

    result = request.GET.get('result', '')
    if result != 'success':
        return False

    pid = request.GET.get('pid', '')

    # get payment stub from the db
    stub = PaymentStub.objects.filter(user=request.user, pid=pid).first()
    if stub == None:
        return False

    payment_ref = request.GET.get('ref', '')

    # verify checksum from the external payment service
    checksumstr = "pid={}&ref={}&result={}&token={}".format(
        pid, payment_ref, result, settings.SELLER_SECRET_KEY)

    # If amount exists in the request and is zero, checkout bypassed the payment
    # service, i.e. there are only free games. Checksum will be the same as in
    # prepare_payment_form above.
    amount = request.GET.get('amount', None)
    if amount != None:
        try:
            # conversion might fail in case of a faulty request
            amount = float(amount)
        except:
            return False

        checksumstr = "pid={}&sid={}&amount={}&token={}".format(
            pid, settings.SELLER_ID, amount, settings.SELLER_SECRET_KEY)

    md5_hash = md5(checksumstr.encode("ascii"))
    checksum = md5_hash.hexdigest()

    received_checksum = request.GET.get('checksum', '')

    if received_checksum != checksum:
        print("does not match")
        return False

    item_ids = json.loads(stub.cart_str)
    games = Game.objects.filter(pk__in=item_ids)
    user = request.user

    # create a new order
    new_order = Order(user=user, payment_ref=payment_ref)
    new_order.save()

    # create a purchase for each game and link to the new order
    # and the user's owner games
    for game in games:
        new_purchase = Purchase(
            game=game, order=new_order, user=user, price=game.price)
        new_purchase.save()
        user.owned_games.add(game)

    # clear cart
    cart_utils.clear_cart(request)

    return True
