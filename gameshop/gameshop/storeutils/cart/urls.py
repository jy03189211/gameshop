from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/(?P<item_id>\d+)/$', views.add_to_cart_view, name="cart_add"),
    url(r'^remove/(?P<item_id>\d+)/$', views.remove_from_cart_view, name="cart_remove"),
]