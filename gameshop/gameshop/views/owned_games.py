from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import render


@method_decorator(login_required, name='dispatch')
class OwnedGamesView(View):

    def get(self, request):
        games = request.user.owned_games.all()
        return render(request, "owned_games.html", { "games": games })
