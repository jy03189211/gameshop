from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import render
from gameshop.models import Game

class GameView(View):

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, game_id):
        game = Game.objects.get(pk=game_id)
        return render(request, "game.html", { "game": game })