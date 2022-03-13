# Imports
# 3rd party:
from django.shortcuts import render
# -----------------------------------------------------------------------------


def products(request):
    """
    View to render the products page, handle sorting and search queries
        Arguments: request (object): HTTP request object
        Returns: render products page with context
    """
    return render(request, 'products/index.html')
