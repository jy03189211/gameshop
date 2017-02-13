from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views, authenticate, login
from django.shortcuts import render, redirect
from gameshop.forms.user import RegisterForm, LoginForm


def login_view_get(request):
    # get page for login and registration
    register_form = RegisterForm(request.GET)
    form = LoginForm(request.GET)
    return render(request, 'login.html', {
        'register_form': register_form,
        'form': form
    })


def login_view(request):

    # if GET, do the login page
    if request.method == 'GET':
        return login_view_get(request)

    # if POST, redirect to the django built-in login view
    if request.method == 'POST':
        register_form = RegisterForm(request.GET)
        return auth_views.login(
            request, template_name='login.html', extra_context={
                'register_form': register_form
            }
        )


def register_view(request):

    # if GET, do the login page, since on the same page with login
    if request.method == 'GET':
        return login_view_get(request)

    # if POST, register a new user
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save(commit=False)
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']

            # if the two password inputs match
            register_form.clean_password2()
            # if the username input is valid and unique
            register_form.clean_username()
            user.set_password(user.password)
            user.generate_api_key()
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        # try again, something went wrong
        return render(request, 'login.html', {
            'register_form': register_form,
            'form': LoginForm()
        })
