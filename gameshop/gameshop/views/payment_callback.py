from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from gameshop.models import Game
from gameshop.storeutils.checkout import checkout as checkout_utils


@login_required
def payment_success_view(request):
    """Handles a successful payment"""

    payment_handled_successfully = checkout_utils.handle_payment_success(request)

    if payment_handled_successfully:

        stub = request.session.get('payment_stub', None)
        if stub == None:
            return redirect('payment_error')

        purchased_ids = stub[1]
        purchased_games = Game.objects.filter(pk__in=purchased_ids)

        # clear stub, not needed after this point
        del request.session['payment_stub']

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

    return render(request, 'payment_callback_cancel.html', {
        'payment_ref': payment_ref
    })


@login_required
def payment_error_view(request):
    """Handles payment errors"""

    payment_ref = request.GET.get('ref', None)

    return render(request, 'payment_callback_error.html', {
        'payment_ref': payment_ref
    })
