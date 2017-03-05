from django import forms
from gameshop.models import Category

class SearchForm(forms.Form):
    name = forms.CharField(label="Name", required=False, max_length=50)
    price_min = forms.DecimalField(label="Price min", required=False, min_value=0.0, max_value=1000.0, decimal_places=2)
    price_max = forms.DecimalField(label="Price max", required=False, min_value=0.0, max_value=1000.0, decimal_places=2)
    created_by = forms.CharField(label="Developer", required=False, max_length=50)
    category = forms.ModelChoiceField(label="Category", required=False,
        queryset=Category.objects.all())
