from django.views.generic import TemplateView
from ..forms.user import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import *
from django.contrib import auth

def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)

class LoginView(TemplateView):

    # def get_context_data(self, **kwargs):
    #     context=super(LoginView, self).get_context_data(**kwargs)
    #     context['registerForm']=RegisterForm(prefix='register')
    #     context['loginForm']=LoginForm(prefix='login')
    #     return context

    def get(self, request, *args, **kwargs):
        registerForm = RegisterForm(request.GET)
        loginForm=LoginForm(request.GET)
        return render(request, 'login.html', {'registerForm': registerForm,'loginForm':loginForm})

    def post(self, request):
        loginForm = LoginForm(request.POST)
        registerForm = RegisterForm(request.POST)
        if 'loginBtn' in request.POST:
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index')


        elif 'registerBtn' in request.POST:
            if registerForm.is_valid():
                user = registerForm.save(commit=False)
                username = registerForm.cleaned_data['username']
                password = registerForm.cleaned_data['password']

                # if the two password inputs match
                registerForm.clean_password2()
                # if the username input is valid and unique
                registerForm.clean_username()
                user.set_password(user.password)
                user.save()
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('index')


        #print('try again')
        return render(request, 'login.html', {'registerForm': registerForm,'loginForm':loginForm})
