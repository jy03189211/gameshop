from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from . import cart
from gameshop.models import Game

@require_POST
def add_to_cart_view(request, item_id):
    item = Game.objects.filter(pk=item_id).first()
    # if no game, 404
    if item == None:
        return HttpResponseNotFound("No such game")
    if cart.add_to_cart(request, item_id):
        return JsonResponse(cart.get_cart(request), safe=False)
    else:
        return HttpResponseServerError("Something went wrong")

@require_POST
def remove_from_cart_view(request, item_id):
    if cart.remove_from_cart(request, item_id):
        # removes if the item was in cart, but no errors if not
        return JsonResponse(cart.get_cart(request), safe=False)
    else:
        return HttpResponseServerError("Something went wrong")
