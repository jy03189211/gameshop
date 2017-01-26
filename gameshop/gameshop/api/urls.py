from django.conf.urls import url
from django.contrib import admin
from gameshop.api import views

urlpatterns = [

    #Game related
    url(r"^game/$", views.games),
    url(r"^game/(?P<game_id>[0-9]+)/$", views.game_single),
    url(r"^game/(?P<game_id>[0-9]+)/score/$", views.game_score, name='game_score'),

    #User related
    url(r"^user/$", views.users, name='user'), #isDeveloper
    url(r"^user/(?P<user_id>[0-9]+)/$", views.user_single, name='user'), #isDeveloper

    url(r"^user/(?P<user_id>[0-9]+)/inventory/$", views.user_inventory, name='user_inventory'), #POST
    url(r"^user/(?P<user_id>[0-9]+)/inventory/?P<game_id>[0-9]+/$", views.user_inventory, name='user_inventory'),

    url(r"^user/(?P<user_id>[0-9]+)/purchased/$", views.user_purchased, name='user_purchased'),
    url(r"^user/(?P<user_id>[0-9]+)/purchased/?P<game_id>[0-9]+/$", views.user_purchased, name='user_purchased'),

    url(r"^user/(?P<user_id>[0-9]+)/sale/$", views.user_sale, name='user_sale'),
    url(r"^user/(?P<user_id>[0-9]+)/sale/?P<sale_id>[0-9]+/$", views.user_sale, name='user_sale'),

    url(r"^user/(?P<user_id>[0-9]+)/order/$", views.user_order, name='user_order'),
    url(r"^user/(?P<user_id>[0-9]+)/order/?P<order_id>[0-9]+/$", views.user_order, name='user_order'),

    url(r"^user/(?P<user_id>[0-9]+)/savegame/$", views.user_savegames, name='user_savegames'),
    url(r"^user/(?P<user_id>[0-9]+)/savegame/?P<game_id>[0-9]+/$", views.user_savegame_single_game, name='user_savegame_single_game'),
    url(r"^user/(?P<user_id>[0-9]+)/savegame/?P<game_id>[0-9]+/?P<savegame_id>[0-9]+/$", views.user_game_savegame, name='user_game_savegame'),

    url(r"^user/(?P<user_id>[0-9]+)/score/$", views.user_score, name='user_score'),

]
