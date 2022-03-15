# Imports
# 3rd party:
from django.shortcuts import render, redirect
# -----------------------------------------------------------------------------


def view_cart(request):
    """
    View to render the shopping cart page.
        Arguments: request (object): HTTP request object
        Returns: render shopping cart page
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """
    View to add the product to the shopping cart stored in session cookies.
        Arguments:
            request (object): HTTP request object
            product_id: ID of product from the form
        Returns:
            redirect_url: Redirect back to product_detail view
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
