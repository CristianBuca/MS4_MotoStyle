# Imports
# 3rd Party
from django.shortcuts import render, get_object_or_404
# Internal
from .models import UserProfile
# -----------------------------------------------------------------------------


def profile(request):
    """
    Displays the user's profile
        Arguments: request (object): The request object
        Return: Render user's profile page
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
