def add_to_cart(request, item_id, item_price):
    cart = request.session.get('cart', {})
    if not item_id in cart:
        cart[str(item_id)] = item_price
        request.session['cart'] = cart
    return True

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart.pop(item_id, None)
    #request.session['cart'] = cart
    return True

def get_cart(request):
    cart = request.session.get('cart', {})
    return cart