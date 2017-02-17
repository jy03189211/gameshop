from itsdangerous import URLSafeTimedSerializer as utsr
import base64
import re

from django.conf import settings as django_settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views, authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from gameshop.forms.user import RegisterForm, LoginForm
from gameshop.models import User


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
            email = register_form.cleaned_data['email']

            # if the two password inputs match
            register_form.clean_password2()

            # if the username input is valid and unique
            register_form.clean_username()
            register_form.clean_email()
            user.set_password(user.password)
            user.generate_api_key()
            token = token_confirm.generate_validate_token(username)
            message = "\n".join([
                u'Dear customer {0},'.format(username),
                u'\nPlease click the following link to validate your account.',
                '/'.join([django_settings.DOMAIN,'activate', token])])

            send_mail(
                'Validation',
                message,
                'admin@gameshop.com',
                [email],
                fail_silently=False,
            )

            user.is_active = False
            user.save()
            #user = authenticate(username=username, password=password)

            if user is not None:
                #login(request, user)
                return render(request, 'generic.html', {
                    'title': 'Registration',
                    'message': 'Please check your email to activate your account. \
                        You can login after activation.'
                })

        # try again, something went wrong
        return render(request, 'login.html', {
            'register_form': register_form,
            'form': LoginForm()
        })

@ensure_csrf_cookie
def activate_user(request, token):

    try:
        username = token_confirm.confirm_validate_token(token)
    except:
        username = token_confirm.remove_validate_token(token)
        users = User.objects.filter(username=username)
        for user in users:
            user.delete()

        return render(request, 'generic.html', {
            'title': 'Error',
            'message': 'Sorry, the link is over due. Please register again.'
        })

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return render(request, 'generic.html', {
            'title': 'Error',
            'message': 'Sorry, the user does not exist!'
        })

    if user.is_active:
        title = 'Information'
        message = 'User already active.'
    else:
        user.is_active = True
        user.save()
        title = 'Success'
        message = 'User activated! You can now login.'

    return render(request, 'generic.html', {
        'title': title,
        'message': message
    })


class Token:
    def __init__(self, security_key):
        self.security_key = security_key
        self.salt = base64.encodebytes(security_key.encode())

    def generate_validate_token(self, username):
        serializer = utsr(self.security_key)
        return serializer.dumps(username, self.salt)

    def confirm_validate_token(self, token, expiration=3600):
        serializer = utsr(self.security_key)
        return serializer.loads(token, salt=self.salt, max_age=expiration)

    def remove_validate_token(self, token):
        serializer = utsr(self.security_key)
        print(serializer.loads(token, salt=self.salt))
        return serializer.loads(token, salt=self.salt)


token_confirm = Token(django_settings.SECRET_KEY)