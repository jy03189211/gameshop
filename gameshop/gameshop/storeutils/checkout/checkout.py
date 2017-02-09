import uuid
from hashlib import md5
from gameshop.forms.payment import PaymentForm
from gameshop.storeutils.cart import cart as cart_utils
from gameshop.settings import SELLER_ID, SELLER_SECRET_KEY


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
            pid, SELLER_ID, amount, SELLER_SECRET_KEY)

        md5_hash = md5(checksumstr.encode("ascii"))
        checksum = md5_hash.hexdigest()

        payment_form = PaymentForm(initial={
            'pid': pid, 'sid': SELLER_ID, 'amount': amount, 'checksum': checksum
        })

        return payment_form

    return None
