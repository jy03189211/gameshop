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

        import pprint
        pprint.pprint(category_groups)

        # lowercase English alphabet
        alphabet = list(string.ascii_lowercase)

        return render(request, "categories.html", {
            'category_groups': category_groups,
            'first_letters': first_letters,
            'alphabet': alphabet
        })