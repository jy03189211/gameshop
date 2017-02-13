import re
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from gameshop.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(
        label='Retype password', widget=forms.PasswordInput())
    is_developer = forms.BooleanField(
        label='Become a developer?', required=False,
        help_text='Developers can add and sell games in the store.')
    public_name = forms.CharField(max_length=50,
        label='Public developer name', required=False,
        help_text='The public name will be shown as the developer\'s name for the games you add.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password',
                  'password2', 'is_developer', 'public_name']

    def clean_password2(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password2 = self.cleaned_data['password2']
            if password == password2:
                return password
        raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError(
                'Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username', max_length=30, widget=forms.TextInput())
    password = forms.CharField(
        label='Password', max_length=30, widget=forms.PasswordInput())

