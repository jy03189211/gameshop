from django import forms
from django.shortcuts import render
from django.views.generic import View

class NewGameForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    url = forms.CharField(label="URL", required=True)
    price = forms.DecimalField(label="Price", min_value=0.0, max_value=1000.0, decimal_places=1)
    available = forms.BooleanField(label="Available for purchase")
    categories = forms.CharField(label="Categories")

class NewGameView(View):

    def get(self, request):
        form = NewGameForm()
        return render(request, "new_game.html", {"form": form})
