from django import forms
from gameshop.models import Game, Category


class NewGameForm(forms.Form):
    name = forms.CharField(label="Name", required=True, max_length=50)
    url = forms.CharField(label="URL", required=True, max_length=200)
    description = forms.CharField(label="Description",
        required=True, max_length=500, widget=forms.Textarea)
    price = forms.DecimalField(
        label="Price", min_value=0.0, max_value=1000.0, decimal_places=2)
    image = forms.FileField(label="Image")
    category = forms.ModelChoiceField(label="Category", required=True,
        queryset=Category.objects.all())
    available = forms.BooleanField(label="Available for purchase")


class EditGameForm(NewGameForm):
    image = forms.FileField(label="Image", required=False)
    # TODO: fix categories and remove this after
