from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class SearchView(TemplateView):
    template_name = "search.html"

class CategoriesView(TemplateView):
    template_name = "categories.html"

class LeaderboardsView(TemplateView):
    template_name = "leaderboards.html"

class YourGamesView(TemplateView):
    template_name = "yourgames.html"