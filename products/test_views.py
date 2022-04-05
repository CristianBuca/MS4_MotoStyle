# Imports
# Internal
from products.models import Product
# 3rd party:
from django.test import TestCase
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

    def test_get_add_product(self):
        """
        Tests if add_product page is accessible with status code of 200
        Tests if add_product view renders add_product.html
        """
        response = self.client.get(f'/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')
