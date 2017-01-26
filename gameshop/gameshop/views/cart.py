from django.views.generic import TemplateView
from django.shortcuts import render
from gameshop.storeutils.cart import cart

class CartView(TemplateView):

    def get(self, request):
        items = cart.get_cart(request)
        total = 0
        for name, price in items.items():
            total += price
        return render(request, "cart.html", {
            'items': items,
            'total': total
        })
