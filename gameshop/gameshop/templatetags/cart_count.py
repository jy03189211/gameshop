from django import template
from gameshop.storeutils.cart import cart

register = template.Library()

@register.simple_tag(takes_context=True)
def cart_count(context):
    """Returns the number of items in the cart"""
    try:
        request = context['request']
        count = len(cart.get_cart(request))
        return count
    except:
        return 0
    return 0
