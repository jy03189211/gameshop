from django.views.generic import TemplateView

class ManagedGamesView(TemplateView):
    template_name = "managed_games.html"