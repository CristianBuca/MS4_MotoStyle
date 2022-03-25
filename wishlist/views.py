# Imports
# 3rd party:
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from django.contrib import messages
# Internal
from products.models import Product
# -----------------------------------------------------------------------------


def view_wishlist(request):
    """
    View to display the user's wishlist
        Arguments: request (object): The request object
        Returns: Render the user's wishlist page
    """

    return render(request, 'wishlist/wishlist.html')
