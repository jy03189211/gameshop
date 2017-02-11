from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^score/$', views.score_view, name="score"),
    url(r'^save/$', views.save_view, name="save"),
    url(r'^load_request/$', views.load_request_view, name="load_request"),
]
