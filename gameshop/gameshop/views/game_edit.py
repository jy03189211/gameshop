from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import View
from gameshop.models import Game
from gameshop.forms.game import EditGameForm
import base64


@method_decorator(login_required, name='dispatch')
class GameEditView(View):

    template_name = "game_edit.html"

    def get(self, request, game_id):
        # get game based on id
        game = get_object_or_404(Game, pk=game_id)

        initial = {
            'name': game.name,
            'url': game.url,
            'description': game.description,
            'price': game.price,
            'available': game.available,
            'category': game.category,
        }

        # NewGameForm for edit with initial population
        form = EditGameForm(initial=initial)

        return render(request, self.template_name, {"game": game, "form": form})

    def post(self, request, game_id):
        # get game based on id
        game = get_object_or_404(Game, pk=game_id)

        # form based on request
        form = EditGameForm(request.POST, request.FILES)

        if form.is_valid():
            # update based on form data
            game.url = form.cleaned_data["url"]
            game.name = form.cleaned_data["name"]
            game.description = form.cleaned_data["description"]
            game.price = form.cleaned_data["price"]
            game.available = form.cleaned_data["available"]
            game.category = form.cleaned_data["category"]

            # update image if a new one was given
            image_binary = None
            if request.FILES['image']:
                image_binary = request.FILES['image'].file.read()
                image_binary = base64.b64encode(image_binary)
            game.image_binary = image_binary

            game.save()

            return redirect('managed_games')

        # if form not valid
        return render(request, self.template_name, {"form": form})


@require_POST
@login_required
def remove_game_view(request, game_id):
    """Removes the given game if it is managed by the user logged in"""

    # only allow the user's managed games
    managed_games = Game.objects.filter(created_by=request.user)
    # get the specific game
    game = managed_games.filter(pk=game_id).first()

    if not game:
        return HttpResponseNotFound("Game not found")

    game.delete()

    message = 'Game "' + game.name + '" removed.'

    return render(request, "generic.html", {
        'title': 'Done',
        'message': message
    })
