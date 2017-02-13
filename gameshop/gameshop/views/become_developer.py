from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse


@login_required
def become_developer_view(request):
    """Promote the logged in user to a developer"""

    request.user.is_developer = True
    request.user.save()

    return redirect(reverse('become_developer_done'))


@login_required
def become_developer_done_view(request):
    """Show success message"""

    return render(request, 'become_developer_done.html')