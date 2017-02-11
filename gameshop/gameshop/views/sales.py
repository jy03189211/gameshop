from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import View
from gameshop.models import Order, Purchase


@method_decorator(login_required, name='dispatch')
class SalesView(View):
    """List the order history of the logged in user"""

    def get(self, request):
        # all sales of games by the logged in user
        sales = Purchase.objects.filter(game__created_by__pk=request.user.pk)
        # most recent first, then by game name
        # NOTE: created_at may be too accurate for secondary ordering to work
        sales = sales.order_by('-created_at', Lower('game__name').asc())

        summary = {}
        summary['revenue'] = 0
        for sale in sales:
            summary['revenue'] += sale.price
        summary['num_purchases'] = len(sales)

        return render(request, "sales.html", {
            'sales': sales,
            'summary': summary
        })