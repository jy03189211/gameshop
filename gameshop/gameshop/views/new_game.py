from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from gameshop.models import Game
from gameshop.models import User
from gameshop.forms.game import NewGameForm


class NewGameView(View):

    def get(self, request, *args, **kwargs):
        form = NewGameForm()
        return render(request, "new_game.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = NewGameForm(request.POST, request.FILES)
        if form.is_valid():
            # create game based on form data
            # TODO: fix the user once login is working
            creator = User.objects.get(pk=1) # first test user in testdata
            new_game = Game(
                url=form.cleaned_data["url"],
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                price=form.cleaned_data["price"],
                available=form.cleaned_data["available"],
                created_by=creator,
                image=form.cleaned_data["image"]
            )
            new_game.save()

            # TODO: add failure redirect
            return HttpResponseRedirect("/game/" + str(new_game.pk))

        # if form not valid
        return render(request, self.template_name, {"form": form})
