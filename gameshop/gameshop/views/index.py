from django.shortcuts import render
from django.views.generic import View
from gameshop.models import Game

class IndexView(View):
    template_name = "index.html"

    def get_latest_games(self, n):
        """Gets n most recently added games"""
        return Game.objects.all().order_by('-created_by')[:n]

    def get(self, request):
        # 1 game in jumbo + 4 games featured
        n = 5
        latest_games = self.get_latest_games(n)
        jumbo_game = latest_games[0]
        featured_games = latest_games[1:n]

        return render(request, self.template_name, {
            "jumbo_game": jumbo_game,
            "featured_games": featured_games
        })
