from django.conf.urls import url
from django.contrib import admin
from gameshop.api import views

urlpatterns = [

    #Game related
    url(r"^game/$", views.game_json, name='game'),
    url(r"^game/?P<game_id>[0-9]+/$", views.game_json, name='game'),
    url(r"^game/?P<game_id>[0-9]+/score/$", views.game_score_json, name='game_score'),

    #User related
    url(r"^user/$", views.user_json, name='user'), #isDeveloper
    url(r"^user/?P<user_id>[0-9]+/$", views.user_json, name='user'), #isDeveloper

    url(r"^user/?P<user_id>[0-9]+/inventory/$", views.user_inventory_json, name='user_inventory'), #POST
    url(r"^user/?P<user_id>[0-9]+/inventory/?P<game_id>[0-9]+/$", views.user_inventory_json, name='user_inventory'),

    url(r"^user/?P<user_id>[0-9]+/purchased/$", views.user_purchased_json, name='user_purchased'),
    url(r"^user/?P<user_id>[0-9]+/purchased/?P<game_id>[0-9]+/$", views.user_purchased_json, name='user_purchased'),

    url(r"^user/?P<user_id>[0-9]+/sale/$", views.user_sale_json, name='user_sale'),
    url(r"^user/?P<user_id>[0-9]+/sale/?P<sale_id>[0-9]+/$", views.user_sale_json, name='user_sale'),

    url(r"^user/?P<user_id>[0-9]+/order/$", views.user_order_json, name='user_order'),
    url(r"^user/?P<user_id>[0-9]+/order/?P<order_id>[0-9]+/$", views.user_order_json, name='user_order'),

    url(r"^user/?P<user_id>[0-9]+/savegame/$", views.user_savegame_json, name='user_savegame'),
    url(r"^user/?P<user_id>[0-9]+/savegame/?P<game_id>[0-9]+/$", views.user_savegame_json, name='user_savegame'),
    url(r"^user/?P<user_id>[0-9]+/savegame/?P<game_id>[0-9]+/?P<savegame_id>[0-9]+/$", views.user_game_savegame_json, name='user_game_savegame'),

    url(r"^user/?P<user_id>[0-9]+/score/$", views.user_score_json, name='user_score'),

]
