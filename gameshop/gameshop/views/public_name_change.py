from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from gameshop.forms.public_name import PublicNameForm


@login_required
def public_name_change_view(request):
    """Change the public_name of the logged in user"""

    form = PublicNameForm(request.POST)
    if form.is_valid():
        request.user.public_name = form.cleaned_data['public_name']
        request.user.save()

        return redirect(reverse('public_name_change_done'))

    return redirect(reverse('settings'))


@login_required
def public_name_change_done_view(request):
    """Show success message"""

    return render(request, 'public_name_change_done.html')