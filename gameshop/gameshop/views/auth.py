from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views, authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from gameshop.forms.user import RegisterForm, LoginForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

@ensure_csrf_cookie
def login_view_get(request):
    # get page for login and registration

    # if no earlier submissions, don't try to build from previous data
    # in order to not show errors at first page load
    register_form = RegisterForm(request.GET or None)
    form = LoginForm(request.GET or None)

    return render(request, 'login.html', {
        'register_form': register_form,
        'form': form
    })


@ensure_csrf_cookie
def login_view(request):

    # if GET, do the login page
    if request.method == 'GET':
        return login_view_get(request)

    # if POST, user the django built-in login view
    if request.method == 'POST':
        register_form = RegisterForm()
        return auth_views.login(
            request, template_name='login.html', extra_context={
                'register_form': register_form
            }
        )


@ensure_csrf_cookie
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
            email=register_form.cleaned_data['email']
            # if the two password inputs match
            register_form.clean_password2()
            # if the username input is valid and unique
            register_form.clean_username()
            register_form.clean_email()
            user.set_password(user.password)
            user.generate_api_key()
            send_mail(
                'Validation',
                'Dear customer, \n\nPlease click the following link to validate your account.',
                'admin@gameshop.com',
                [email],
                fail_silently=False,
            )
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

def ValidateEmail( email ):
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False