from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
import json

from gameshop.models import *


def user_score_json(request, user_id):

    return HttpResponse('', content_type="application/json")

def user_game_savegame_json(request, user_id, game_id, savegame_id):

    return HttpResponse('', content_type="application/json")

def user_savegame_json(request, user_id, game_id=None):

    return HttpResponse('', content_type="application/json")

def user_order_json(request, user_id, order_id=None):

    return HttpResponse('', content_type="application/json")

def user_sale_json(request, user_id, sale_id=None):

    return HttpResponse('', content_type="application/json")

def user_purchased_json(request, user_id, game_id=None):

    return HttpResponse('', content_type="application/json")

def user_inventory_json(request, user_id, game_id=None):

    return HttpResponse('', content_type="application/json")

def user_json(request, user_id=None):

    return HttpResponse('', content_type="application/json")

def game_score_json(request, game_id):

    return HttpResponse('', content_type="application/json")

def game_json(request, game_id=None):

    #data = Country.objects.all().filter(continent=continent)
    # countries = {}
    # for country in data:
    #     countries[country.code] = country.name
    # my_json_data = json.dumps(countries)

    if request.method == 'GET':
        get_game(request, game_id)

        # if "callback" in request.GET:
        #     callback = request.GET["callback"]
        #     a = callback + "(" + my_json_data + ")"
        #     return HttpResponse(a, content_type="text/javascript")

    # elif request.method == 'POST':
    #     set_game(request, game_id)
    #

def get_game(request, game_id=None):

    game = get_object_or_404(Game, pk=game_id)

    objects_filtered = Game.objects

    for key in request.GET:
        objects_filtered = objects_filtered.filter(key)

    game_list = list(objects_filtered)

    json_data = json.dumps(game_list)
    # createdBy = request.GET.get('createdby')
    # priceMin = request.GET.get('pricemin')
    # priceMax = request.GET.get('pricemax')
    # available = request.GET.get('available')
    # category = request.GET.get('category')
    # year = request.GET.get('year')
    # month = request.GET.get('month')
    # day = request.GET.get('day')
    # Game.objects.filter(createdBy).filter(available).filter(category).filter(year).filter(month).filter(day)
    return HttpResponse(json_data, content_type="application/json")
# def set_game(request, game_id=None):
