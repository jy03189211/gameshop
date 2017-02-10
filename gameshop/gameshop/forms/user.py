import re
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from gameshop.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput(),)
    password2 = forms.CharField(
        label='retype password', widget=forms.PasswordInput(),)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        write_only_fields = ['password']

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

