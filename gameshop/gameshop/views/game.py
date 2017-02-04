from django.views.generic import View
from django.shortcuts import render
from gameshop.models import Game

class GameView(View):

    def get(self, request, game_id):
        game = Game.objects.get(pk=game_id)
        return render(request, "game.html", { "game": game })