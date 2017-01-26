from django import template
from gameshop.storeutils.cart import cart

register = template.Library()

@register.assignment_tag(takes_context=True)
def cart_count(context):
    try:
        request = context['request']
        count = len(cart.get_cart(request))
        return count
    except:
        pass
    return False
