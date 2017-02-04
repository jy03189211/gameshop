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
from .views import *
from .api.views import *
from .storeutils.cart import urls as cart_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^search/$', SearchView.as_view(), name="search"),
    url(r'^categories/$', CategoriesView.as_view(), name="categories"),
    url(r'^leaderboards/$', LeaderboardsView.as_view(), name="leaderboards"),
    url(r'^your_games/$', DashboardView.as_view(), name="dashboard"),
    url(r'^your_games/dashboard/$', DashboardView.as_view(), name="dashboard"),
    url(r'^your_games/settings/$', SettingsView.as_view(), name="settings"),
    url(r'^your_games/owned_games/$', OwnedGamesView.as_view(), name="owned_games"),
    url(r'^your_games/orders/$', OrdersView.as_view(), name="orders"),
    url(r'^your_games/managed_games/$', ManagedGamesView.as_view(), name="managed_games"),
    url(r'^your_games/sales/$', SalesView.as_view(), name="sales"),
    url(r'^your_games/new_game/$', NewGameView.as_view(), name="new_game"),
    url(r'^game/(?P<game_id>\d+)/$', GameView.as_view(), name="game"),
    url(r'^game/(?P<game_id>\d+)/edit/$', GameEditView.as_view(), name="game_edit"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^loginuser/$',login.login),
    url(r'^register/$', LoginView.as_view(),name='register'),
    url(r'^cart/$', CartView.as_view(), name="cart"),
    url(r'^cart/', include(cart_urls)),
    #third party authentication
    #url(r'^accounts/', include('allauth.urls')),
    #api
    url(r'^api/v1/', include('gameshop.api.urls')),
]


# for development
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)