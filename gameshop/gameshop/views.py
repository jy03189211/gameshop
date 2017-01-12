from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class SearchView(TemplateView):
    template_name = "search.html"

class CategoriesView(TemplateView):
    template_name = "categories.html"

class LeaderboardsView(TemplateView):
    template_name = "leaderboards.html"

class DashboardView(TemplateView):
    template_name = "dashboard.html"

class SettingsView(TemplateView):
    template_name = "settings.html"

class OwnedGamesView(TemplateView):
    template_name = "owned_games.html"

class OrdersView(TemplateView):
    template_name = "orders.html"

class ManagedGamesView(TemplateView):
    template_name = "managed_games.html"

class SalesView(TemplateView):
    template_name = "sales.html"

class NewGameView(TemplateView):
    template_name = "new_game.html"

class GameView(TemplateView):
    template_name = "game.html"