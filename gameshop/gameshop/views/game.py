from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from gameshop.models import Game, Score

class GameView(View):

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, game_id):

        game = get_object_or_404(Game, pk=game_id)

        # top 10 scores for the logged in user
        your_highscores = Score.objects.filter(
            game=game, user=request.user).order_by('-score')[:10]

        # top 10 global leaderboard
        leaderboard = Score.objects.filter(game=game).order_by('-score')[:10]

        return render(request, 'game.html', {
            'game': game,
            'your_highscores': your_highscores,
            'leaderboard': leaderboard
        })