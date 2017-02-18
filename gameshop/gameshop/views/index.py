from django.shortcuts import render
from django.views.generic import View
from gameshop.models import Game


class IndexView(View):

    def get(self, request):
        # 1 game in jumbo + 4 games featured
        n = 5

        # get the n latest available games
        latest_games = Game.objects.filter(available=True)
        latest_games = latest_games.order_by('-created_at')[:n]
        print(len(latest_games))
        
        if len(latest_games) == 0:
            jumbo_game = None
            featured_games = None
        else:
            jumbo_game = latest_games[0]
            featured_games = latest_games[1:n]

        return render(request, 'index.html', {
            "jumbo_game": jumbo_game,
            "featured_games": featured_games
        })
