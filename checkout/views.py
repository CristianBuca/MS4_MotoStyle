# Imports
# 3rd party:
import os
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
# Internal:
from .forms import OrderForm
# -----------------------------------------------------------------------------


def checkout(request):
    stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')
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
        'stripe_public_key': stripe_public_key,
        'client_secret': 'client_secret',
    }

    return render(request, template, context)
