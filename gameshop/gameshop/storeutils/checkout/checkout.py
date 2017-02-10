import uuid
from hashlib import md5
from gameshop.forms.payment import PaymentForm
from gameshop.models import Game, Order, Purchase, User
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

        base_url = request.META['wsgi.url_scheme'] + '://' \
                    + request.META['HTTP_HOST'] + '/'

        payment_form = PaymentForm(
            initial={
                'pid': pid,
                'sid': settings.SELLER_ID,
                'amount': amount,
                'checksum': checksum,
                'success_url': base_url + settings.PAYMENT_SUCCESS_URL,
                'cancel_url': base_url + settings.PAYMENT_CANCEL_URL,
                'error_url': base_url + settings.PAYMENT_ERROR_URL,
            }
        )

        # store stub purchase in session for success handling
        request.session['payment_stub'] = (pid, cart)

        return payment_form

    return None


def handle_payment_success(request):
    """Handles game ownership and purchase history after a successful payment"""

    result = request.GET.get('result', '')
    if result != 'success':
        print("result not success")
        return False

    # get payment stub (tuple (pid, cart))
    stub = request.session.get('payment_stub', None)
    if stub == None:
        print("no stub")
        return False

    pid = stub[0]
    payment_ref = request.GET.get('ref', '')

    # verify checksum
    checksumstr = "pid={}&ref={}&result={}&token={}".format(
        pid, payment_ref, result, settings.SELLER_SECRET_KEY)

    md5_hash = md5(checksumstr.encode("ascii"))
    checksum = md5_hash.hexdigest()

    received_checksum = request.GET.get('checksum', '')

    if received_checksum != checksum:
        print("checksum failed")
        return False

    item_ids = stub[1]
    games = Game.objects.filter(pk__in=item_ids)
    user = request.user

    # create a new order
    new_order = Order(user=user, payment_ref=payment_ref)
    new_order.save()

    # create a purchase for each game and link to the new order
    # and the user's owner games
    for game in games:
        new_purchase = Purchase(game=game, order=new_order, user=user)
        new_purchase.save()
        user.owned_games.add(game)

    # clear cart
    cart_utils.clear_cart(request)

    return True
