from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
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

def users(request):
    filters = User.objects
    username = request.GET.get('username')
    public_name = request.GET.get('public_name')
    is_developer = request.GET.get('is_developer')

    if username != None:
        filters = filters.filter(username = username)
    if public_name != None:
        filters = filters.filter(public_name = public_name)
    if is_developer != None:
        filters = filters.filter(is_developer = is_developer)

    data = filters.all()
    user_dict = {}
    user_list = []
    #Todo construct json
    for user in data:
        user_dict["id"]=user.pk
        user_dict["username"]=user.username
        user_dict["public_name"]=user.public_name
        user_dict["is_developer"]=user.is_developer
        user_list.append(user_dict.copy())

    #user_list_serialized = serializers.serialize('json', data)
    return JsonResponse(user_list, safe=False)

def user_single(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    data = {
    "created_at": user.created_at,
    "updated_at": user.updated_at,
    "username": user.username,
    "public_name": user.public_name,
    "is_developer": user.is_developer,
     }
    return JsonResponse(data)

def game_score(request, game_id):

    return HttpResponse('', content_type="application/json")

#todo finalize owned by attribute
def game_single(request, game_id):

    game = get_object_or_404(Game, pk=game_id)
    print(game)
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
    #"owned_by": game.owned_by,
     }
    return JsonResponse(data)
#todo add price and date logic
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
        game_dict = {}
        game_list = []
        
        for game in data:
            game_dict["id"] = game.pk
            game_dict["name"] = game.name
            game_dict["url"] = game.url
            game_dict["name"] = game.name
            game_dict["description"] = game.description
            game_dict["price"] = game.price
            game_dict["categories"] = game.categories
            game_dict["created_by"] = game.created_by_id
            game_dict["available"] = game.available
            game_list.append(game_dict.copy())
        #print(games)
        return JsonResponse(game_list, safe=False)

    elif request.method == 'POST':
        print("POST")
