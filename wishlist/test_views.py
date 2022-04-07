# Imports
# 3rd Party:
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
# Internal
from wishlist.models import Wishlist
from products.models import Product
# -----------------------------------------------------------------------------


class TestWishlistViews(TestCase):
    """
    Defines the views unit tests for the wishlist app
    """
    def test_get_wishlist(self):
        """
        Tests if wishlist page is accessible with status code of 200
        Tests if wishlist view renders wishlist.html
        """
        user = User.objects.create_user(
                username='unit_test_user', password='unit_test_pass'
            )
        product = Product.objects.create(
                name='Test Product',
                price='123.45',
                description='Test Product Description',
            )
        Wishlist.objects.create(owner=user, product=product)
        wishlist = Wishlist.objects.filter(owner=user, product=product)

        self.client.login(username='unit_test_user', password='unit_test_pass')
        response = self.client.get('/wishlist/', {'wishlist': wishlist})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')

    def test_add_to_wishlist(self):
        """
        Tests success message when user adds to product to wishlist
        Tests error message when user adds product to wishlist twice
        Tests if user is redirected to the product_detail page
        """
        user = User.objects.create_user(
                username='unit_test_user', password='unit_test_pass'
            )
        product_1 = Product.objects.create(
                name='Test Product in Wishlist',
                price='123.45',
                description='Test Product Description',
            )
        product_2 = Product.objects.create(
                name='Test Product',
                price='123.45',
                description='Test Product Description',
            )

        Wishlist.objects.create(owner=user, product=product_1)

        self.client.login(username='unit_test_user', password='unit_test_pass')
        response_success = self.client.get(f'/wishlist/add/{product_2.id}/')
        message_success = list(get_messages(response_success.wsgi_request))
        response_error = self.client.get(f'/wishlist/add/{product_1.id}/')
        message_error = list(get_messages(response_error.wsgi_request))
        self.assertEqual(str(
            message_success[0]), f'Added {product_2.name} to your wishlist'
        )
        self.assertEqual(str(
            message_error[1]), f'{product_1.name} already in your wishlist'
        )
        self.assertRedirects(
            response_success, f'/products/{product_2.id}/'
        )
