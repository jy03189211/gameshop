from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from gameshop.forms.user import RegisterForm, LoginForm


def login_view_get(request):
    # get page for login and registration
    register_form = RegisterForm(request.GET)
    login_form = LoginForm(request.GET) # TODO: use the django view instead of this
    return render(request, 'login.html', {
        'register_form': register_form,
        'login_form': login_form}
    )


def login_view(request):

    # if GET, do the login page
    if request.method == 'GET':
        return login_view_get(request)

    # if POST, redirect to the django built-in login view
    if request.method == 'POST':
        return auth_views.login(request)


def register_view(request):

    # if GET, do the login page, since on the same page with login
    if request.method == 'GET':
        return login_view_get(request)

    # if POST, register a new user
    if request.method == 'POST':
        # do register stuff
        pass

