from django import forms
from gameshop.models import Game


class NewGameForm(forms.Form):
    name = forms.CharField(label="Name", required=True, max_length=50)
    url = forms.CharField(label="URL", required=True, max_length=200)
    description = forms.CharField(label="Description", required=True, max_length=500, widget=forms.Textarea)
    price = forms.DecimalField(label="Price", min_value=0.0, max_value=1000.0, decimal_places=1)
    image = forms.FileField(label="Image")
    categories = forms.CharField(label="Categories")
    available = forms.BooleanField(label="Available for purchase")

class EditGameForm(NewGameForm):
    image = forms.FileField(label="Image", required=False)
    # TODO: fix categories and remove this after
    categories = forms.CharField(label="Categories", required=False)
