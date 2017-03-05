from django.conf.urls import url
from django.contrib import admin
from gameshop.api import views

urlpatterns = [

    #Game related
    url(r"^game/$", views.get_games_json),
    url(r"^game/(?P<game_id>[0-9]+)/$", views.get_games_json),
    url(r"^game/(?P<game_id>[0-9]+)/score/$", views.get_game_score_json, name='game_score'),

    #User related
    url(r"^user/$", views.get_users_json, name='user'),
    url(r"^user/(?P<user_id>[0-9]+)/$", views.get_user_single_json, name='user'),
    url(r"^user/(?P<user_id>[0-9]+)/inventory/$", views.user_inventory, name='user_inventory'),
    url(r"^user/(?P<user_id>[0-9]+)/purchased/$", views.get_user_purchased_json, name='user_purchased'),
    url(r"^user/(?P<user_id>[0-9]+)/sale/$", views.get_user_sale_json, name='user_sale'),
    url(r"^user/(?P<user_id>[0-9]+)/order/$", views.get_user_order_json, name='user_order'),
    url(r"^user/(?P<user_id>[0-9]+)/order/?P<order_id>[0-9]+/$", views.get_user_order_json, name='user_order'),
    url(r"^user/(?P<user_id>[0-9]+)/savegame/$", views.get_user_savegames_json, name='user_savegames'),
    url(r"^user/(?P<user_id>[0-9]+)/savegame/(?P<game_id>[0-9]+)/$", views.get_user_single_game_savegames_json, name='user_savegame_single_game'),
    url(r"^user/(?P<user_id>[0-9]+)/savegame/(?P<game_id>[0-9]+)/(?P<savegame_id>[0-9]+)/$", views.user_game_savegame_json, name='user_game_savegame'),
    url(r"^user/(?P<user_id>[0-9]+)/score/$", views.get_user_score_json, name='user_score_json'),

]
