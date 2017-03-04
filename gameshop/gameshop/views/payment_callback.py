from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from gameshop.models import Game, PaymentStub
from gameshop.storeutils.checkout import checkout as checkout_utils
import json


@login_required
def payment_success_view(request):
    """Handles a successful payment"""

    payment_handled_successfully = checkout_utils.handle_payment_success(request)

    if payment_handled_successfully:

        pid = request.GET.get('pid', '')

        # get payment stub from the db
        stub = PaymentStub.objects.filter(user=request.user, pid=pid).first()
        if stub == None:
            return redirect('payment_error')

        purchased_ids = json.loads(stub.cart_str)
        purchased_games = Game.objects.filter(pk__in=purchased_ids)

        # clear stub, not needed after this point, the same information is
        # stored in the purchase
        stub.delete()

        payment_ref = request.GET.get('ref', '')

        return render(request, 'payment_callback_success.html', {
            'games': purchased_games,
            'payment_ref': payment_ref
        })

    return redirect('payment_error')


@login_required
def payment_cancel_view(request):
    """Handles a cancelled payment"""

    payment_ref = request.GET.get('ref', '')
    pid = request.GET.get('pid', '')

    # if payment was explicitly cancelled, remove the stub
    stub = PaymentStub.objects.filter(user=request.user, pid=pid).first()
    if stub != None:
        stub.delete()

    return render(request, 'payment_callback_cancel.html', {
        'payment_ref': payment_ref
    })


@login_required
def payment_error_view(request):
    """Handles payment errors"""

    payment_ref = request.GET.get('ref', None)
    pid = request.GET.get('pid', None)

    # add the payment reference to the sub and set the error flag,
    # useful for admin investigation
    stub = PaymentStub.objects.filter(user=request.user, pid=pid).first()
    if stub != None:
        stub.error = True
        stub.payment_ref = payment_ref
        stub.save()

    return render(request, 'payment_callback_error.html', {
        'payment_ref': payment_ref,
        'pid': pid
    })
