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

    def test_add_to_cart_no_size_exists(self):
        """
        Tests if user can add same product with no size to the cart twice
        Tests if toast displays correct message
        """
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        self.client.post(
            f'/cart/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_cart'}
        )
        response = self.client.post(
            f'/cart/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_cart'}
        )
        cart = self.client.session['cart']

        self.assertEqual(cart[str(product.id)], 2)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]),
            f'Updated {product.name} quantity to {cart[str(product.id)]}'
        )

    def test_add_to_cart_has_size_exists(self):
        """
        Tests if user can add same product with same size to the cart twice
        Tests if toast displays correct message
        """
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        self.client.post(
            f'/cart/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_cart', 'product_size': 'XS'}
        )
        response = self.client.post(
            f'/cart/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_cart', 'product_size': 'XS'}
        )
        cart = self.client.session['cart']

        self.assertEqual(cart[str(product.id)], {'items_by_size': {'XS': 2}})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]),
            f'Updated size XS {product.name} quantity to 2'
        )

    def test_adjust_cart_has_size(self):
        """
        Tests if user can adjust item with size in cart quantity
        Tests if toast displays correct message
        Tests if user is redirected back to cart view
        """
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        self.client.post(
            f'/cart/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_cart', 'product_size': 'XS'}
        )
        self.client.post(
            f'/cart/adjust/{product.id}/',
            {'quantity': 2, 'redirect_url': 'view_cart', 'product_size': 'XS'}
        )
        response = self.client.post(
            f'/cart/adjust/{product.id}/',
            {'quantity': 0, 'redirect_url': 'view_cart', 'product_size': 'XS'}
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]),
            f'Updated size XS {product.name} quantity to 2'
        )
        self.assertEqual(
            str(messages[2]),
            f'Removed size XS {product.name} from your cart'
        )
        self.assertRedirects(response, '/cart/')

    def test_adjust_cart_no_size(self):
        """
        Tests if user can adjust item without size in cart quantity
        Tests if toast displays correct message
        Tests if user is redirected back to cart view
        """
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        self.client.post(
            f'/cart/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_cart'}
        )
        self.client.post(
            f'/cart/adjust/{product.id}/',
            {'quantity': 2, 'redirect_url': 'view_cart'}
        )
        response = self.client.post(
            f'/cart/adjust/{product.id}/',
            {'quantity': 0, 'redirect_url': 'view_cart'}
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]),
            f'Updated {product.name} quantity to 2'
        )
        self.assertEqual(
            str(messages[2]),
            f'Removed {product.name} from your cart'
        )
        self.assertRedirects(response, '/cart/')

    def test_remove_from_cart_no_size(self):
        """
        Tests if user can remove item without size from cart
        Tests if toast displays correct message
        """
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        self.client.post(
            f'/cart/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_cart'}
        )
        response = self.client.post(f'/cart/remove/{product.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]),
            f'Removed {product.name} from your cart'
        )

    def test_remove_from_cart_has_size(self):
        """
        Tests if user can remove item with size from cart
        Tests if toast displays correct message
        """
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        self.client.post(
            f'/cart/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_cart', 'product_size': 'XS'}
        )
        response = self.client.post(
            f'/cart/remove/{product.id}/', {'product_size': 'XS'}
        )
        cart = self.client.session['cart']
        self.assertEqual(cart, {})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]),
            f'Removed size XS {product.name} from your cart'
        )

    def test_remove_from_cart_exception(self):
        """
        Tests the HttpResponse for trying to remove
        invalid item from cart is 500
        Tests if toasts displays correct error message.
        """
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        response = self.client.post(f'/cart/remove/{product.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 500)
        self.assertEqual(str(messages[0]), 'Error removing item: (e)')
