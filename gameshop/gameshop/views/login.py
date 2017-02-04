from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from gameshop.forms.user import UserForm


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.save()
            user = authenticate(username=username, password1=password)
            context = {
                'form': form,
            }
            return render(request, 'login.html', context)
        return render(request, 'login.html', {'form': form})
