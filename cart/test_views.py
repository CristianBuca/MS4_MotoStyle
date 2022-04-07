# Imports
# 3rd party:
from django.test import TestCase
# -----------------------------------------------------------------------------


class TestCartViews(TestCase):
    """
    Defines the views unit tests for the cart app
    """
    def test_get_view_cart(self):
        """
        Tests if cart page is accessible with status code of 200
        Tests if cart view renders cart.html
        """
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('cart/cart.html')
