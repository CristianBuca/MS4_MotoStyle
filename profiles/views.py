# Imports
# 3rd Party
from django.shortcuts import render, get_object_or_404
# Internal
from .models import UserProfile
from .forms import UserProfileForm
# -----------------------------------------------------------------------------


def profile(request):
    """
    Displays the user's profile
        Arguments: request (object): The request object
        Return: Render user's profile page
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
