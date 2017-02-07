from django.views.generic import TemplateView
from django.shortcuts import render
from gameshop.storeutils.cart import cart
from gameshop.models import Game

class CartView(TemplateView):

    def get(self, request):
        item_ids = cart.get_cart(request)
        total = 0

        games_in_cart = Game.objects.filter(id__in=item_ids)

        for game in games_in_cart:
            total += game.price

        return render(request, "cart.html", {
            'games': games_in_cart,
            'total': total
        })
