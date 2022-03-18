# Imports
# 3rd party:
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
# Internal:
from .forms import OrderForm
# -----------------------------------------------------------------------------


def checkout(request):
    """
    Defines the checkout view
        Arguments: request (object): The checkout request
        Returns: render of checkout page
    """

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your shopping cart is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
