import string
from django.shortcuts import render
from django.views.generic import View
from gameshop.models import Category


class CategoriesView(View):
    """Shows all existing game categories"""

    def get(self, request):
        categories = Category.objects.all()

        # build groups by first letters
        category_groups = {}
        for cat in categories:
            # if key exists, append to list at it, else create and append
            category_groups.setdefault(cat.name[0], []).append(cat)

        first_letters = list(category_groups.keys())

        # make all lowercase to ignore case when compared to alphabet
        category_groups = dict((k.lower(), v) for k, v in category_groups.items())
        first_letters = [l.lower() for l in first_letters]

        # lowercase English alphabet
        alphabet = list(string.ascii_lowercase)

        return render(request, "categories.html", {
            'category_groups': category_groups,
            'first_letters': first_letters,
            'alphabet': alphabet
        })