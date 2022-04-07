# Imports
# 3rd Party:
from django.test import TestCase
from django.contrib.auth.models import User
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
