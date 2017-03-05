from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import *
import base64, binascii, hashlib, json, os
from gameshop.decorators import require_api_key

from gameshop.models import *

#High scores for user filtered by game.
def get_user_score(user_id, game_id=None):

    filters = Score.objects.filter(user__pk=user_id)

    if game_id != None:
        filters = filters.filter(game__pk = game_id)

    data = list(filters.order_by('-score'))
    return data

@require_api_key
def get_user_score_json(request, user_id):

    user = User.objects.get(pk=request.user.id)
    request_api_key = request.META['HTTP_API_KEY']
    user_api_key = user.api_key

    if does_api_key_match(request_api_key, user_api_key) == False:
        return HttpResponse('Unauthorized', status=401)

    if host_is_allowed(request, user) == False:
        return HttpResponse('Unauthorized', status=401)


    if request.method == 'GET':
        game_id = request.GET.get('gameid')

        data = get_user_score(user_id, game_id)

        score_dict = {}
        score_list = []

        for score in data:
            score_dict["id"] = score.pk
            score_dict["game"] = score.game.name
            score_dict["user"] = score.user.username

            score_list.append(score_dict.copy())

        return JsonResponse(score_list, safe=False)

    return HttpResponse('', content_type="application/json")


# A single savegame
@require_api_key
def user_game_savegame_json(request, user_id, game_id, savegame_id):

    user = User.objects.get(pk=request.user.id)
    request_api_key = request.META['HTTP_API_KEY']
    user_api_key = user.api_key

    if does_api_key_match(request_api_key, user_api_key) == False:
        return HttpResponse('Unauthorized', status=401)

    if host_is_allowed(request, user) == False:
        return HttpResponse('Unauthorized', status=401)


    if request.method == 'GET':
        savegame = get_object_or_404(Savegame, pk=savegame_id)
        data = {
        "id": savegame.pk,
        "created_at": savegame.created_at,
        "updated_at": savegame.updated_at,
        "data": savegame.data,
        "game": savegame.game.name,
        "user": savegame.user.username,
         }
        return JsonResponse(data)

    return HttpResponse('', content_type="application/json")

#All the saved games for a user for a single game
@require_api_key
def get_user_single_game_savegames_json(request,user_id, game_id):

    user = User.objects.get(pk=request.user.id)
    request_api_key = request.META['HTTP_API_KEY']
    user_api_key = user.api_key

    if does_api_key_match(request_api_key, user_api_key) == False:
        return HttpResponse('Unauthorized', status=401)

    if host_is_allowed(request, user) == False:
        return HttpResponse('Unauthorized', status=401)


    if request.method == 'GET':

        savegames=list(Savegame.objects.filter(user__pk=user_id).filter(game__pk=game_id).order_by('-updated_at'))
        savegame_dict = {}
        savegame_list = []

        for savegame in savegames:

            savegame_dict["id"] = savegame.pk
            savegame_dict["data"] = savegame.data
            savegame_dict["game"] = savegame.game.name
            savegame_dict["user"] = savegame.user.username
            savegame_list.append(savegame_dict.copy())

        return JsonResponse(savegame_list, safe=False)

    return HttpResponse('', content_type="application/json")

#Get all savegames for user or post new savegame
@require_api_key
def get_user_savegames_json(request, user_id, game_id=None):

    user = User.objects.get(pk=request.user.id)
    request_api_key = request.META['HTTP_API_KEY']
    user_api_key = user.api_key

    if does_api_key_match(request_api_key, user_api_key) == False:
        return HttpResponse('Unauthorized', status=401)

    if host_is_allowed(request, user) == False:
        return HttpResponse('Unauthorized', status=401)


    if request.method == 'GET':

        savegames=list(Savegame.objects.filter(user__pk=user_id).order_by('-updated_at'))
        savegame_dict={}
        savegame_list=[]
        for savegame in savegames:

            savegame_dict["id"] = savegame.pk
            savegame_dict["data"] = savegame.data
            savegame_dict["game"] = savegame.game.name
            savegame_dict["user"] = savegame.user.username
            savegame_list.append(savegame_dict.copy())

        return JsonResponse(savegame_list, safe=False)

    elif request.method == 'POST':
        received_json = ''
        if request.content_type == 'application/json':
            received_json = json.loads(request.body.decode("utf-8"))

        if received_json['data'] != None:
            data = received_json['data']

        if received_json['game_id'] != None:
            game = get_object_or_404(Game, pk=received_json['game_id'])

        user = get_object_or_404(User, pk=user_id)

        savegame = Savegame(data=data, game=game, user=user)
        savegame.save()

    return HttpResponse('', content_type="application/json")
    # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#Return all orders for an user or a single order
@require_api_key
def get_user_order_json(request, user_id, order_id=None):

    user = User.objects.get(pk=request.user.id)
    request_api_key = request.META['HTTP_API_KEY']
    user_api_key = user.api_key

    if does_api_key_match(request_api_key, user_api_key) == False:
        return HttpResponse('Unauthorized', status=401)

    if host_is_allowed(request, user) == False:
        return HttpResponse('Unauthorized', status=401)


    if order_id == None:
        orders=list(Order.objects.filter(user__pk=user_id).order_by('-updated_at'))
        order_dict={}
        order_list=[]
        for order in orders:

            order_dict["id"] = order.pk
            order_dict["user"] = order.user.username
            order_dict["payment_ref"] = order.payment_ref
            order_list.append(order_dict.copy())

        return JsonResponse(order_list, safe=False)

    else:
        order = get_object_or_404(Order, pk=order_id)
        data = {
        "id": order.pk,
        "created_at": order.created_at,
        "updated_at": order.updated_at,
        "user": order.user.username,
        "payment_ref": order.payment_ref,
         }
        return JsonResponse(data)

@require_api_key
def get_user_sale_json(request, user_id):

    user = User.objects.get(pk=request.user.id)
    request_api_key = request.META['HTTP_API_KEY']
    user_api_key = user.api_key

    if does_api_key_match(request_api_key, user_api_key) == False:
        return HttpResponse('Unauthorized', status=401)

    if host_is_allowed(request, user) == False:
        return HttpResponse('Unauthorized', status=401)


    user = get_object_or_404(User, pk=user_id)
    sales=list(Purchase.objects.filter(game__created_by=user_id, user__pk=user_id))
    sale_dict = {}
    sale_list = []

    for sale in sales:

        sale_dict["id"] = sale.pk
        sale_dict["game"] = sale.game.name
        sale_dict["sale_id"] = sale.order.pk
        sale_dict["user"] = sale.user.name

        sale_list.append(sale_dict.copy())

    return JsonResponse(sale_list, safe=False)

@require_api_key
def get_user_purchased_json(request, user_id):

    user = User.objects.get(pk=request.user.id)
    request_api_key = request.META['HTTP_API_KEY']
    user_api_key = user.api_key

    if does_api_key_match(request_api_key, user_api_key) == False:
        return HttpResponse('Unauthorized', status=401)

    if host_is_allowed(request, user) == False:
        return HttpResponse('Unauthorized', status=401)


    user = get_object_or_404(User, pk=user_id)
    purchased=list(Purchase.objects.filter(game__owned_by=user_id, user__pk=user_id))
    purchased_dict = {}
    purchased_list = []

    for purchase in purchased:

        purchased_dict["id"] = purchase.pk
        purchased_dict["game"] = purchase.game.name
        purchased_dict["order_id"] = purchase.order.pk
        purchased_dict["user"] = purchase.user.name

        purchased_list.append(purchased_dict.copy())

    return JsonResponse(purchased_list, safe=False)

#Add game to inventory or get games from inventory
@require_api_key
def user_inventory(request, user_id):

    user = User.objects.get(pk=request.user.id)
    request_api_key = request.META['HTTP_API_KEY']
    user_api_key = user.api_key

    if does_api_key_match(request_api_key, user_api_key) == False:
        return HttpResponse('Unauthorized', status=401)

    if host_is_allowed(request, user) == False:
        return HttpResponse('Unauthorized', status=401)


    if request.method == 'GET':

        inventory = Game.objects.filter(owned_by__pk=user_id).order_by('-name')
        data = serializers.serialize("json", inventory)
        return HttpResponse(data, content_type='application/json')

    elif request.method == 'POST':
        received_json = ''
        game = ''

        if(request.content_type == 'application/json'):
            received_json = json.loads(request.body.decode("utf-8"))

        if(received_json['game_id'] != None):
            game = get_object_or_404(Game, pk=received_json['game_id'])

        user = get_object_or_404(User, pk=user_id)
        user.owned_games.add(game)

        return HttpResponse('', content_type="application/json")

#Get all users
@require_api_key
def get_users_json(request):

    user = User.objects.get(pk=request.user.id)
    request_api_key = request.META['HTTP_API_KEY']
    user_api_key = user.api_key

    if does_api_key_match(request_api_key, user_api_key) == False:
        return HttpResponse('Unauthorized', status=401)

    if host_is_allowed(request, user) == False:
        return HttpResponse('Unauthorized', status=401)


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

    return JsonResponse(user_list, safe=False)

#Get single user
@require_api_key
def get_user_single_json(request, user_id):

    user = User.objects.get(pk=request.user.id)
    request_api_key = request.META['HTTP_API_KEY']
    user_api_key = user.api_key

    if does_api_key_match(request_api_key, user_api_key) == False:
        return HttpResponse('Unauthorized', status=401)

    if host_is_allowed(request, user) == False:
        return HttpResponse('Unauthorized', status=401)


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

#Get score list of a single game
@require_api_key
def get_game_score_json(request, game_id):

    user = User.objects.get(pk=request.user.id)
    request_api_key = request.META['HTTP_API_KEY']
    user_api_key = user.api_key

    if does_api_key_match(request_api_key, user_api_key) == False:
        return HttpResponse('Unauthorized', status=401)

    if host_is_allowed(request, user) == False:
        return HttpResponse('Unauthorized', status=401)


    scores=list(Score.objects.filter(game__pk=game_id).order_by('-score'))
    score_dict = {}
    score_list = []

    for score in scores:
        score_dict["id"] = score.pk
        score_dict["created_at"] = score.created_at
        score_dict["updated_at"] = score.updated_at
        score_dict["score"] = score.score
        score_dict["game"] = score.game.name
        score_dict["user"] = score.user.username
        score_list.append(score_dict.copy())

    return JsonResponse(score_list, safe=False)

#Returns all games with given parameters
def get_games(filter_dict):

    filters = Game.objects

    if filter_dict['pk'] != None:
        filters = filters.filter(pk = filter_dict['pk'])
    if filter_dict['name'] != None:
        filters = filters.filter(name__icontains=filter_dict['name'])
    if filter_dict['price_min'] != None:
        filters = filters.filter(price__gte=filter_dict['price_min'])
    if filter_dict['price_max'] != None:
        filters = filters.filter(price__lte=filter_dict['price_max'])
    if filter_dict['created_by'] != None:
        filters = filters.filter(created_by__public_name__icontains=filter_dict['created_by'])
    if filter_dict['category'] != None:
        filters = filters.filter(category=filter_dict['category'])
    if filter_dict['year'] != None:
        filters = filters.filter(created_at__year=filter_dict['year'])
    if filter_dict['available'] != None:
        filters = filters.filter(available=filter_dict['available'])

    data = list(filters.order_by('-name'))

    return data

@require_api_key
def get_games_json(request, game_id=None):

    user = User.objects.get(pk=request.user.id)
    request_api_key = request.META['HTTP_API_KEY']
    user_api_key = user.api_key

    if does_api_key_match(request_api_key, user_api_key) == False:
        return HttpResponse('Unauthorized', status=401)

    if host_is_allowed(request, user) == False:
        return HttpResponse('Unauthorized', status=401)


    if request.method == 'GET':
        filter_dict={}

        if game_id != None:
            filter_dict['pk'] = game_id
        else:
            filter_dict['pk'] = None

        filter_dict['name'] = request.GET.get('name')
        filter_dict['price_min'] = request.GET.get('price_min')
        filter_dict['price_max'] = request.GET.get('price_max')
        filter_dict['created_by'] = request.GET.get('created_by')
        filter_dict['category'] = request.GET.get('category')
        filter_dict['year'] = request.GET.get('year')
        filter_dict['available'] = request.GET.get('available')

        game_list = get_games(filter_dict)

        data = serializers.serialize("json", game_list)
        return HttpResponse(data, content_type='application/json')

    return HttpResponse('', content_type="application/json")

# Check if user host is in the list of allowed hosts
def host_is_allowed(request, user):
    user_allowed_hosts = user.get_api_host_list()
    host = request.META['HTTP_HOST']
    if host != None:
        if user.api_hosts == '*':
            return True
        for allowed_host in user_allowed_hosts:
            if host == allowed_host:
                return True
        return False

# Check if api_key matches to the one got from database
def does_api_key_match(request_api_key, user_api_key):

    decoded_key = base64.b64decode(request_api_key)
    api_key_parts = decoded_key.split(bytes('::','utf-8'))

    request_username = api_key_parts[0].decode('utf-8')
    user = User.objects.get(username=request_username)
    if user != None:
        if request_username == user.username and request_api_key == user_api_key:
            return True
    else:
        return False
