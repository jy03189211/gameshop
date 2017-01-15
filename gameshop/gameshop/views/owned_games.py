from django.views.generic import TemplateView

class OwnedGamesView(TemplateView):
    template_name = "owned_games.html"