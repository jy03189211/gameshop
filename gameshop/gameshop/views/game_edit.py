from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import View
from gameshop.models import Game
from gameshop.forms.game import EditGameForm


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
            if form.cleaned_data["image"]:
                game.image = form.cleaned_data["image"]

            game.save()

            # TODO: add failure redirect
            return HttpResponseRedirect("/game/" + str(game.pk))

        # if form not valid
        return render(request, self.template_name, {"form": form})
