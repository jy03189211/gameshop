from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import View
from gameshop.models import Game
import base64


class GameImageView(View):

    def get(self, request, game_id):
        """Return the game image, if exists"""

        game = get_object_or_404(Game, pk=game_id)

        if game.image_binary:
            image_data = base64.b64decode(game.image_binary)

            # determine content type based on the first characters
            content_type = 'image/jpeg'
            if b'PNG' in image_data[0:10]:
                content_type = 'image/png'

            return HttpResponse(image_data, content_type)

        return Http404()