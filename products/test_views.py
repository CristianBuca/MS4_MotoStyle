# Imports
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
# Internal
from products.models import Product
# -----------------------------------------------------------------------------


class TestProductsViews(TestCase):
    """
    Defines the views unit tests for the products app
    """
    def test_get_products(self):
        """
        Tests if products page is accessible with status code of 200
        Tests if products view renders products.html
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail(self):
        """
        Tests if product_detail page is accessible with status code of 200
        Tests if product_detail view renders product_detail.html
        """
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_user_get_add_product(self):
        """
        Tests if regular user is redirected to landing page when trying to
        access add_product page with status code of 302
        """
        user = User.objects.create_user(
            username='unit_test_user', password='unit_test_pass'
        )
        self.client.login(username='unit_test_user', password='unit_test_pass')
        response = self.client.get('/products/add/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertEqual(str(
            messages[0]), 'Sorry this feature is for store owners only.'
        )
