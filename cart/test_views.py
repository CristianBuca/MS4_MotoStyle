# Imports
# 3rd party:
from django.test import TestCase
from django.contrib.messages import get_messages
# Internal
from products.models import Product
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

    def test_add_to_cart_no_size(self):
        """
        Tests if user is able to add a product with no size to the cart
        Tests if toast displays correct message
        """
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        response = self.client.post(
            f'/cart/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_cart'}
        )
        cart = self.client.session['cart']
        self.assertEqual(cart[str(product.id)], 1)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), f'Added {product.name} to your cart'
        )

    def test_add_to_cart_has_size(self):
        """
        Tests if user is able to add a product with size to the cart
        Tests if toast displays correct message
        """
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        response = self.client.post(
            f'/cart/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_cart', 'product_size': 'XS'}
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), f'Added size XS {product.name} to your cart'
        )
