from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from gameshop.forms import RegisterForm, LoginForm


def login_view_get(request):
    # get page for login and registration
    register_form = RegisterForm(request.GET)
    login_form = LoginForm(request.GET) # TODO: use the django view instead of this
    return render(request, 'login.html', {'registerForm': registerForm,'loginForm':loginForm})


def login_view(request):

    # if GET, do the login page
    if request.method == 'GET':
        return login_view_get(request)

    # if POST, redirect to the django built-in login view
    if request.method == 'POST':
        return auth_views.login(register)


def register_view(request):

    # if GET, do the login page, since on the same page with login
    if request.method == 'GET':
        return login_view_get(request)

    # if POST, register a new user
    if request.method == 'POST':
        # do register stuff