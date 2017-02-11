from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from gameshop.models import Game, Score, Savegame


def _check_type_and_attribute(request, required_type, required_attribute=None):
    """
    Validates that the request has the required type and
    that the required attribute exists
    """

    message_type = request.POST.get('messageType', None)
    if message_type != required_type:
        return False

    if required_attribute != None:
        attribute_value = request.POST.get(required_attribute, None)
        if attribute_value == None:
            return False

    return True


@require_POST
@login_required
def score_view(request, game_id):
    """Saves a score sent from a game"""

    if not _check_type_and_attribute(request, 'SCORE', 'score'):
        # TODO: handle error
        pass

    score = request.POST.get('score', None)
    game = Game.objects.filter(pk=game_id).first()
    if not game:
        return JsonResponse({
            'messageType': 'ERROR',
            'info': 'Game not found'
        }, status=404)

    new_score = Score(score=score, game=game, user=request.user)
    new_score.save()

    return JsonResponse({
        'messageType': 'OK',
        'info': 'Score saved'
    })


@require_POST
@login_required
def save_view(request, game_id):
    """
    Saves a game state sent from a game. Overrides an existing
    savegame for the combination (game, user). I.e. only the
    latest savegame is stored.
    """

    if not _check_type_and_attribute(request, 'SAVE', 'gameState'):
        # TODO: handle error
        pass

    data = request.POST.get('gameState', None)
    game = Game.objects.filter(pk=game_id).first()
    if not game:
        return JsonResponse({
            'messageType': 'ERROR',
            'info': 'Game not found'
        }, status=404)

    # if already exists, update
    existing_savegame = Savegame.objects.filter(
        game=game, user=request.user).first()
    if existing_savegame:
        existing_savegame.data = data
        return JsonResponse({
            'messageType': 'OK',
            'info': 'Savegame updated'
        })

    # otherwise create a new one
    new_savegame = Savegame(data=data, game=game, user=request.user)
    new_savegame.save()
    return JsonResponse({
        'messageType': 'OK',
        'info': 'Savegame created'
    })


@require_POST
@login_required
def load_request_view(request, game_id):
    """Responds with savegame data for the given (game, user) combination"""

    if not _check_type_and_attribute(request, 'LOAD_REQUEST'):
        # TODO: handle error
        pass

    game = Game.objects.filter(pk=game_id).first()
    if not game:
        return JsonResponse({
            'messageType': 'ERROR',
            'info': 'Game not found'
        }, status=404)

    savegame = Savegame.objects.filter(game=game, user=request.user).first()
    if not savegame:
        return JsonResponse({
            'messageType': 'ERROR',
            'info': 'Savegame not found'
        }, status=404)

    game_state = savegame.data

    return JsonResponse({
        'messageType': 'LOAD',
        'gameState': game_state
    })