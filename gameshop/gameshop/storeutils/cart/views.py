from django.http import HttpResponse, HttpResponseServerError
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from . import cart

@require_POST
def add_to_cart_view(request, item_id):
    # TODO: get item price
    item_price = 0
    if cart.add_to_cart(request, item_id, item_price):
        return JsonResponse(cart.get_cart(request))
    else:
        return HttpResponseServerError("Something went wrong")

@require_POST
def remove_from_cart_view(request, item_id):
    if cart.remove_from_cart(request, item_id):
        return HttpResponse("Item removed")
    else:
        # TODO: implement something more sensible
        return HttpResponseServerError("Something went wrong")
