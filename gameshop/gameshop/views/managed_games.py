from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from gameshop.models import Game


@method_decorator(login_required, name='dispatch')
class ManagedGamesView(View):
    """List the managed games of the logged in user"""

    def get(self, request):

        # games that the user has created
        games = Game.objects.filter(created_by=request.user)

        return render(request, 'managed_games.html', {
            'games': games
        })
