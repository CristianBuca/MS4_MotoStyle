# Imports
# 3rd party:
from django.shortcuts import render, redirect, reverse
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
        Arguments:
            request (object): HTTP request object
            item_id: ID of product from the form
        Returns:
            redirect_url: Redirect back to product_detail view
    """

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
            else:
                cart[item_id]['items_by_size'][size] = quantity
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

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

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
        else:
            del cart[item_id]['items_by_size'][size]
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
