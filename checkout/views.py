# Imports
# 3rd party:
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
import stripe
# Internal:
from .forms import OrderForm
from cart.contexts import cart_contents
# -----------------------------------------------------------------------------


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    """
    Defines the checkout view
        Arguments: request (object): The checkout request
        Returns: render of checkout page
    """

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your shopping cart is empty")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key missing.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
