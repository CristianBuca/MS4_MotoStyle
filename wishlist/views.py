# Imports
# 3rd party:
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Internal
from products.models import Product
from .models import Wishlist
# -----------------------------------------------------------------------------


@login_required
def view_wishlist(request):
    """
    View to display the user's wishlist
        Arguments: request (object): The request object
        Returns: Render the user's wishlist page
    """
    owner = get_object_or_404(User, id=request.user.id)
    wishlist = Wishlist.objects.filter(owner=owner)

    context = {
        'wishlist': wishlist,
    }
    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    View to add a product to the user's wishlist
        Arguments:
            request (object): The request object
            product_id: The id of the product to be added
        Return: Product detail page
    """
    owner = get_object_or_404(User, id=request.user.id)
    product = get_object_or_404(Product, pk=product_id)

    Wishlist.objects.create(owner=owner, product=product)
    messages.success(request, f'Added {product.name} to your wishlist')

    return redirect(reverse('product_detail', args=[product_id]))
