"""gameshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from gameshop.views import *
from gameshop.api.views import *
from gameshop.message_service import urls as message_urls
from gameshop.storeutils.cart import urls as cart_urls
from gameshop import settings
#from gameshop.views import auth
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^search/$', SearchView.as_view(), name="search"),
    url(r'^categories/$', CategoriesView.as_view(), name="categories"),
    url(r'^your_games/$', RedirectView.as_view(pattern_name='owned_games', permanent=True), name="your_games"),
    url(r'^your_games/settings/$', SettingsView.as_view(), name="settings"),
    url(r'^your_games/owned_games/$', OwnedGamesView.as_view(), name="owned_games"),
    url(r'^your_games/orders/$', OrdersView.as_view(), name="orders"),
    url(r'^your_games/orders/(?P<order_id>\d+)/$', OrdersView.as_view(), name="order"),
    url(r'^your_games/managed_games/$', ManagedGamesView.as_view(), name="managed_games"),
    url(r'^your_games/sales/$', SalesView.as_view(), name="sales"),
    url(r'^your_games/new_game/$', NewGameView.as_view(), name="new_game"),
    url(r'^game/(?P<game_id>\d+)/$', GameView.as_view(), name="game"),
    url(r'^game/(?P<game_id>\d+)/edit/$', GameEditView.as_view(), name="game_edit"),
    url(r'^game/(?P<game_id>\d+)/remove/$', remove_game_view, name="game_remove"),
    url(r'^game/(?P<game_id>\d+)/', include(message_urls)),
    url(r'^cart/$', CartView.as_view(), name="cart"),
    url(r'^cart/', include(cart_urls)),

    # profile settings
    url(r'^public_name_change/$',
        public_name_change_view, name="public_name_change"),
    url(r'^public_name_change_done/$',
        public_name_change_done_view, name="public_name_change_done"),
    url(r'^become_developer/$',
        become_developer_view, name="become_developer"),
    url(r'^become_developer_done/$',
        become_developer_done_view, name="become_developer_done"),
    url(r'^update_api_settings/$',
        update_api_settings_view, name="update_api_settings"),
    url(r'^update_api_settings_done/$',
        update_api_settings_done_view, name="update_api_settings_done"),

    # payment service callback handling
    url(r'^' + settings.PAYMENT_SUCCESS_URL + '$', payment_success_view),
    url(r'^' + settings.PAYMENT_CANCEL_URL + '$', payment_cancel_view),
    url(r'^' + settings.PAYMENT_ERROR_URL + '$', payment_error_view),

    #third party authentication
    #login cancel page overriding
    url(r'^accounts/social/login/cancelled/$', RedirectView.as_view(pattern_name='login', permanent=False), name='facebook_login_cancel'),
    url(r'^accounts/', include('allauth.urls')),

    #api
    url(r'^api/v1/', include('gameshop.api.urls')),

    # authentication
    url(r'^register/$', register_view, name='register'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^activate/(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$',auth.activate_user,name='active_user'),
    # password change utilizing the django built-in views with custom templates
    url(r'^password_change/$', auth_views.password_change, {
        'template_name': 'password_change.html'
    }, name='password_change'),
    # give success message as extra context
    url(r'^password_change_done/$', auth_views.password_change_done, {
        'template_name': 'settings_done.html',
        'extra_context': {
            'message': 'Password successfully changed.'
        }
    }, name='password_change_done'),

]


# for development
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)