from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
import json

from gameshop.models import *


def user_score(request, user_id):

    return HttpResponse('', content_type="application/json")

def user_game_savegame(request, user_id, game_id, savegame_id):

    return HttpResponse('', content_type="application/json")

def user_savegame_single_game(request, game_id):

    return HttpResponse('', content_type="application/json")

def user_savegames(request, user_id):

    return HttpResponse('', content_type="application/json")

def user_order(request, user_id, order_id=None):

    return HttpResponse('', content_type="application/json")

def user_sale(request, user_id, sale_id=None):

    return HttpResponse('', content_type="application/json")

def user_purchased(request, user_id, game_id=None):

    return HttpResponse('', content_type="application/json")

def user_inventory(request, user_id, game_id=None):

    return HttpResponse('', content_type="application/json")

def users(request, user_id=None):

    return HttpResponse('', content_type="application/json")

def user_single(request, user_id=None):

    return HttpResponse('', content_type="application/json")

def game_score(request, game_id):

    return HttpResponse('', content_type="application/json")

def game_single(request, game_id):

    game = get_object_or_404(Game, pk=game_id)
    data = {
    "created_at": game.created_at,
    "updated_at": game.updated_at,
    "url": game.url,
    "name": game.name,
    "description": game.description,
    "price": game.price,
    "available": game.available,
    "categories": game.categories,
    "created_by": game.created_by.public_name,
    #"owned_by": game.owned_by.all(),
     }
    return JsonResponse(data)

def games(request):

    if request.method == 'GET':
        filters = Game.objects

        created_by = request.GET.get('createdby')
        available = request.GET.get('available')
        name = request.GET.get('name')
        priceMin = request.GET.get('pricemin')
        priceMax = request.GET.get('pricemax')
        categories = request.GET.get('categories')
        year = request.GET.get('year')
        month = request.GET.get('month')
        day = request.GET.get('day')

        if created_by != None:
            filters = filters.filter(created_by = created_by)

        if available != None:
            filters = filters.filter(available = available)

        if categories != None:
            filters = filters.filter(categories = categories)

        if year != None:
            print('year')

        data = filters.all()
        games = {}
        for game in data:
            games[game.id] = game.name
        #print(games)
        return JsonResponse(games)

    elif request.method == 'POST':
        print("POST")
