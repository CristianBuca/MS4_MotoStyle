# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render

def index(request):
    """
    View to render the index page.
        Arguments: request (object): HTTP request object
        Returns: render index page
    """
    return render(request, 'home/index.html')
