from django.views.generic import View
from django.shortcuts import render

class OwnedGamesView(View):

    def get(self, request):
        games = request.user.owned_games.all()
        return render(request, "owned_games.html", { "games": games })
