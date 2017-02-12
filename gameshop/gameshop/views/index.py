from django.shortcuts import render
from django.views.generic import View
from gameshop.models import Game


def get_latest_games(n):
    """Gets n most recently added games"""
    return Game.objects.all().order_by('-created_at')[:n]


class IndexView(View):

    def get(self, request):
        # 1 game in jumbo + 4 games featured
        n = 5
        latest_games = get_latest_games(n)

        jumbo_game = latest_games[0]
        featured_games = latest_games[1:n]

        return render(request, 'index.html', {
            "jumbo_game": jumbo_game,
            "featured_games": featured_games
        })
