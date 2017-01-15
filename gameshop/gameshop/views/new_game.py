from django.views.generic import TemplateView

class NewGameView(TemplateView):
    template_name = "new_game.html"