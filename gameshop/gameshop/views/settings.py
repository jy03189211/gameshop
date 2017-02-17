from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import View
from gameshop.forms.api_settings import ApiSettingsForm
from gameshop.forms.public_name import PublicNameForm


@method_decorator(login_required, name='dispatch')
class SettingsView(View):

    def get(self, request):

        # If there are forms with errors stored in session, use those,
        # otherwise create empty forms.
        # In addition, if there are errors, jump directly to the correct
        # form with the anchor.

        anchor = None

        public_name_form_data = request.session.get('public_name_form', None)
        if public_name_form_data != None:
            anchor = 'developer_settings'
            # cleanup
            del request.session['public_name_form']

        public_name_form = PublicNameForm(public_name_form_data or {
            'public_name': request.user.public_name
        })

        api_settings_form_data = request.session.get('api_settings_form', None)
        if api_settings_form_data != None:
            anchor = 'api_settings'
            # cleanup
            del request.session['api_settings_form']

        api_settings_form = ApiSettingsForm(api_settings_form_data or {
            'api_hosts': request.user.api_hosts
        })

        return render(request, "settings.html", {
            'public_name_form': public_name_form,
            'api_settings_form': api_settings_form,
            'anchor': anchor
        })


@login_required
def become_developer_view(request):
    """Promote the logged in user to a developer"""

    request.user.is_developer = True
    request.user.save()

    return redirect(reverse('become_developer_done'))


@login_required
def become_developer_done_view(request):
    """Show success message"""

    return render(request, 'settings_done.html', {
        'message': 'You are now a developer.'
    })


@login_required
def public_name_change_view(request):
    """Change the public_name of the logged in user"""

    form = PublicNameForm(request.POST)
    if form.is_valid():
        request.user.public_name = form.cleaned_data['public_name']
        request.user.save()

        return redirect(reverse('public_name_change_done'))

    # if not valid, put form data with errors in session and
    # redirect back to settings
    request.session['public_name_form'] = request.POST
    return redirect(reverse('settings'))


@login_required
def public_name_change_done_view(request):
    """Show success message"""

    return render(request, 'settings_done.html', {
        'message': 'Public name changed.'
    })


@login_required
def update_api_settings_view(request):
    """Change the api settings of the logged in user"""

    form = ApiSettingsForm(request.POST)

    if form.is_valid():
        request.user.api_hosts = form.cleaned_data['api_hosts']
        request.user.save()
        return redirect(reverse('update_api_settings_done'))

    # if not valid, put form data with errors in session and
    # redirect back to settings
    request.session['api_settings_form'] = request.POST
    return redirect(reverse('settings'))


@login_required
def update_api_settings_done_view(request):
    """Show success message"""

    return render(request, 'settings_done.html', {
        'message': 'API settings updated.'
    })