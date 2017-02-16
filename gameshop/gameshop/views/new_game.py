import base64
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from gameshop.models import Game
from gameshop.models import User
from gameshop.forms.game import NewGameForm


@method_decorator(login_required, name='dispatch')
class NewGameView(View):

    def get(self, request, *args, **kwargs):
        form = NewGameForm()
        return render(request, "new_game.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = NewGameForm(request.POST, request.FILES)
        if form.is_valid():

            # Store image in the database as base64.
            # NOTE: Naturally, large images may be sluggish and this is not a
            #       recommended practice. Better store and serve media from a
            #       server designed for that purpose. Like S3.

            image_binary = None
            if request.FILES['image']:
                image_binary = request.FILES['image'].file.read()
                image_binary = base64.b64encode(image_binary)

            # create game based on form data
            new_game = Game(
                url=form.cleaned_data["url"],
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                price=form.cleaned_data["price"],
                available=form.cleaned_data["available"],
                created_by=request.user,
                category=form.cleaned_data["category"],
                image_binary=image_binary
            )
            new_game.save()

            # creator always owns the game also
            request.user.owned_games.add(new_game)
            request.user.save()

            return HttpResponseRedirect("/game/" + str(new_game.pk))

        # if form not valid
        return render(request, self.template_name, {"form": form})
