from django.views.generic import View
from django.shortcuts import render
from gameshop.models import Game

class OwnedGamesView(View):

    def get(self, request):
        games = Game.objects.all()
        return render(request, "owned_games.html", { "games": games })
