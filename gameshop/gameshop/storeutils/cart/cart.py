from gameshop.models import Game

def add_to_cart(request, item_id):
    """Adds the given item ID to the current session's cart"""
    # the cart is a list of ID's
    cart = request.session.get('cart', [])
    if not item_id in cart:
        cart.append(item_id)
        request.session['cart'] = cart
    return True

def remove_from_cart(request, item_id):
    """Removed the given item ID from the current session's cart"""
    cart = request.session.get('cart', [])
    if item_id in cart:
        cart.remove(item_id)
    request.session['cart'] = cart
    return True

def get_cart(request):
    """Returns a list of item ID's in the cart"""
    cart = request.session.get('cart', [])
    return cart

def get_cart_total(request):
    """Returns the cart total price"""
    total = 0
    item_ids = get_cart(request)
    games_in_cart = Game.objects.filter(id__in=item_ids)
    for game in games_in_cart:
        total += game.price
    return total

def clear_cart(request):
    """Resets the cart"""
    request.session['cart'] = []