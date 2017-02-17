import datetime
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import View
from gameshop.models import Game, Order, Purchase


@method_decorator(login_required, name='dispatch')
class SalesView(View):
    """List the order history of the logged in user"""

    def get(self, request):

        # games the user has added
        managed_games = Game.objects.filter(
            created_by=request.user).order_by('name')

        # filter down based on dropdown value
        selected_games = managed_games
        selected_pk = request.GET.get('game', None)
        if selected_pk and selected_pk != '' and selected_pk != 'all':
            selected_games = selected_games.filter(pk=selected_pk)

        # ensure int for the dropdown conditional in template
        try:
            selected_pk = int(selected_pk)
        except:
            selected_pk = -1

        # all sales of games by the logged in user
        sales = Purchase.objects.filter(game__in=selected_games)
        # most recent first
        sales = sales.order_by('-created_at')

        summary = {}

        # revenue total
        summary['revenue'] = 0
        for sale in sales:
            summary['revenue'] += sale.price

        # number of purchases in total
        summary['num_purchases'] = len(sales)

        # datetime 30 days ago
        thirty_days_ago = datetime.date.today() - datetime.timedelta(days=30)
        sales_last30d = sales.filter(created_at__gte=thirty_days_ago)

        # revenue last 30 days
        summary['revenue_last30d'] = 0
        for sale in sales_last30d:
            summary['revenue_last30d'] += sale.price

        # num of sales last 30 days
        summary['num_purchases_last30d'] = len(sales_last30d)

        return render(request, "sales.html", {
            'managed_games': managed_games,
            'selected_pk': selected_pk,
            'sales': sales,
            'summary': summary
        })