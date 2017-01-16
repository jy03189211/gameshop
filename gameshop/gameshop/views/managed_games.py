from django.views.generic import View
from django.shortcuts import render
from gameshop.models import Game

class ManagedGamesView(View):

    def get(self, request):
        games = Game.objects.all()
        return render(request, "managed_games.html", { "games": games })
