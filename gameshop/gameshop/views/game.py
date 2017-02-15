from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View
from gameshop.models import Game, Score


@method_decorator(login_required, name='dispatch')
class GameView(View):

    def get(self, request, game_id):

        game = get_object_or_404(Game, pk=game_id)

        # top 10 scores for the logged in user
        your_highscores = Score.objects.filter(
            game=game, user=request.user).order_by('-score')[:10]

        # top 10 global leaderboard
        leaderboard = Score.objects.filter(game=game).order_by('-score')[:10]

        # already owned
        owned = False
        owned_games = request.user.owned_games.all()
        if game in owned_games:
            owned = True

        return render(request, 'game.html', {
            'game': game,
            'your_highscores': your_highscores,
            'leaderboard': leaderboard,
            'owned': owned
        })
