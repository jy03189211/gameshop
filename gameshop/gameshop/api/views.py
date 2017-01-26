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
    user = get_object_or_404(User, pk=user_id)
    purchased=list(Purchase.objects.filter(game__owned_by=user_id, user__pk=user_id ))
    purchased_dict = {}
    purchased_list = []

    for purchase in purchased:

        purchased_dict["id"] = purchase.pk
        purchased_dict["game"] = purchase.game.name
        purchased_dict["order_id"] = purchase.order.pk
        purchased_dict["user"] = purchase.user.name

        purchased_list.append(purchased_dict.copy())

    return JsonResponse(purchased_list, safe=False)


def user_inventory(request, user_id, game_id=None):

    user = get_object_or_404(User, pk=user_id)
    inventory=list(Game.objects.filter(owned_by__pk=user_id).order_by('-name'))
    inventory_dict = {}
    inventory_list = []

    for game in inventory:

        inventory_dict["id"] = game.pk
        inventory_dict["name"] = game.name
        inventory_dict["url"] = game.url
        inventory_dict["description"] = game.description
        inventory_dict["price"] = game.price
        inventory_dict["categories"] = game.categories
        inventory_dict["created_by"] = game.created_by_id
        inventory_dict["available"] = game.available
        inventory_list.append(inventory_dict.copy())

    return JsonResponse(inventory_list, safe=False)

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
    "id": user.pk,
    "created_at": user.created_at,
    "updated_at": user.updated_at,
    "username": user.username,
    "public_name": user.public_name,
    "is_developer": user.is_developer,
     }
    return JsonResponse(data)

def game_score(request, game_id):

    game = get_object_or_404(Game, pk=game_id)
    scores=list(Score.objects.filter(game__pk=game_id).order_by('-score'))
    score_dict = {}
    score_list = []

    for score in scores:
        score_dict["score"] = score.score
        score_dict["game"] = game.name
        score_list.append(score_dict.copy())

    return JsonResponse(score_list, safe=False)

#todo finalize owned by attribute
def game_single(request, game_id):

    game = get_object_or_404(Game, pk=game_id)

    data = {
    "id": game.pk,
    "created_at": game.created_at,
    "updated_at": game.updated_at,
    "url": game.url,
    "name": game.name,
    "description": game.description,
    "price": game.price,
    "available": game.available,
    "categories": game.categories,
    "created_by": game.created_by.public_name,
    # "owned_by": game.owned_by,
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

        return JsonResponse(game_list, safe=False)

    elif request.method == 'POST':
        print("POST")
