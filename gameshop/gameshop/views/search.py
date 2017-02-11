from django.shortcuts import render
from django.views.generic import View
from gameshop.models import Game
from gameshop.forms.search import SearchForm


class SearchView(View):
    template_name = "search.html"

    def get(self, request):

        # TODO: very similar to the API code,
        # separate json and object api functions and then change this to use it
        #-------

        filters = Game.objects

        created_by = request.GET.get('created_by')
        available = request.GET.get('available')
        name = request.GET.get('name')
        price_min = request.GET.get('price_min')
        price_max = request.GET.get('price_max')
        category = request.GET.get('category')

        # TODO: public or not? availability always or not
        filters.filter(available=True)

        # optional filters
        if name != None:
            filters = filters.filter(name__icontains=name)
        if price_min:
            filters = filters.filter(price__gte=price_min)
        if price_max:
            filters = filters.filter(price__lte=price_max)
        if created_by != None:
            filters = filters.filter(created_by__public_name__icontains=created_by)
        if category != None:
            filters = filters.filter(category=category)


        # if available != None:
        #     filters = filters.filter(available = available)
        # if year != None:
        #     print('year')

        data = filters.all()

        #-------

        results = data

        form = SearchForm(initial=request.GET.dict())

        return render(request, self.template_name, {
            "results": results,
            "form": form
        })
