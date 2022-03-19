# Imports
# 3rd Party
from django.shortcuts import render
# -----------------------------------------------------------------------------


def profile(request):
    """
    Displays the user's profile
        Arguments: request (object): The request object
        Return: Render user's profile page
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
