from django.views.generic import TemplateView
from django.shortcuts import render
from gameshop.storeutils.cart import cart as cart_utils
from gameshop.storeutils.checkout import checkout as checkout_utils
from gameshop.models import Game


class CartView(TemplateView):

    def get(self, request):
        item_ids = cart_utils.get_cart(request)
        games_in_cart = Game.objects.filter(id__in=item_ids)
        total = cart_utils.get_cart_total(request)
        payment_form = checkout_utils.prepare_payment_form(request)

        return render(request, "cart.html", {
            'games': games_in_cart,
            'total': total,
            'payment_form': payment_form
        })
