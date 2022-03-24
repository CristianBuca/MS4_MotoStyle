# Imports
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

    