# Imports
# 3rd party:
from django.test import TestCase
from django.contrib.messages import get_messages
# -----------------------------------------------------------------------------


class TestCheckoutViews(TestCase):
    """
    Defines the views unit tests for the checkout app
    """
    def test_get_checkout_empty_cart(self):
        """
        Tests if user is redirected to products page when trying to access
        checkout with an empty cart and status code is 302
        Tests if toast displays correct error message
        """

        response = self.client.get('/checkout/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')
        self.assertEqual(str(messages[0]), 'Your shopping cart is empty')
