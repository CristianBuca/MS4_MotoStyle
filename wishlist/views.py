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
        Return: Redirect to product detail page
    """
    owner = get_object_or_404(User, id=request.user.id)
    product = get_object_or_404(Product, pk=product_id)

    if not Wishlist.objects.filter(owner=owner, product=product):
        Wishlist.objects.create(owner=owner, product=product)
        messages.success(request, f'Added {product.name} to your wishlist')
    else:
        messages.error(request, f'{product.name} already in your wishlist')

    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_from_wishlist(request, product_id):
    """
    View to remove a product from the user's wishlist
        Arguments:
            request (object): The request object
            product_id: The id of the product to be added
        Return: Render wishlist page
    """
    owner = get_object_or_404(User, id=request.user.id)
    product = get_object_or_404(Product, pk=product_id)

    Wishlist.objects.filter(owner=owner, product=product).delete()
    messages.success(request, f'Removed {product.name} from your wishlist')

    return redirect(reverse('product_detail', args=[product_id]))
