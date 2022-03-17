# Imports
# 3rd party:
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from django.contrib import messages
# Internal
from products.models import Product
# -----------------------------------------------------------------------------


def view_cart(request):
    """
    View to render the shopping cart page.
        Arguments: request (object): HTTP request object
        Returns: render shopping cart page
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    View to add the product to the shopping cart stored in session cookies.
    Includes appropriate message with each call
        Arguments:
            request (object): HTTP request object
            item_id: ID of product from the form
        Returns:
            redirect_url: Redirect back to product_detail view
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, f'Updated size {size} {product.name} quantity to '
                    f'{cart[item_id]["items_by_size"][size]}'
                )
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'Added size {size} {product.name} to your cart'
                )
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'Added size {size} {product.name} to your cart'
            )

    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}'
            )

        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    View to adjust the quantity of the product in the shopping
    cart stored in session cookies.
        Arguments:
            request (object): HTTP request object
            item_id: ID of product from the form
        Returns:
            redirect_url: Redirect back to product_detail view
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, f'Updated size {size} {product.name} quantity to '
                f'{cart[item_id]["items_by_size"][size]}'
            )
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                messages.success(
                    request, f'Removed size {size} {product.name}'
                    'from your cart'
                )
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}'
            )
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    View remove the product from the shopping cart stored in session cookies.
        Arguments:
            request (object): HTTP request object
            item_id: ID of product from the form
        Returns:
            HttpResponse: 200
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request, f'Removed size {size.upper()} '
                f'{product.name} from your cart'
            )
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: (e)')
        return HttpResponse(status=500)
