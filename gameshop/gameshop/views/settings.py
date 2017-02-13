from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from gameshop.forms.public_name import PublicNameForm


@method_decorator(login_required, name='dispatch')
class SettingsView(View):

    def get(self, request):

        public_name_form = PublicNameForm(initial={
            'public_name': request.user.public_name
        })

        return render(request, "settings.html", {
            'public_name_form': public_name_form
        })
