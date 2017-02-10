from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import View
from gameshop.models import Order, Purchase


@method_decorator(login_required, name='dispatch')
class OrdersView(View):
    """List the order history of the logged in user"""

    def get(self, request, order_id=None):
        orders = Order.objects.filter(user__exact=request.user.pk)

        selected_order = None
        if order_id:
            selected_order = get_object_or_404(Order, pk=order_id)

        return render(request, "orders.html", {
            'orders': orders,
            'selected_order': selected_order
        })
