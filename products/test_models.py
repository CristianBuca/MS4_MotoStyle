# Imports
# 3rd party:
from django.test import TestCase
# Internal
from .models import Category, Product
# -----------------------------------------------------------------------------


class TestProductsModels(TestCase):
    """
    Defines the models unit tests for the products app
    """

    def test_category_str(self):
        """
        Tests if Category model str method returns correct string
        """
        category = Category.objects.create(
            name='unit_test_category',
            friendly_name='Unit Test Category',
            description='unit test description',
        )
        self.assertEqual(category.__str__(), category.name)

    def test_category_friendly(self):
        """
        Tests if Category model get_friendly_name returns correct string
        """
        category = Category.objects.create(
            name='unit_test_category',
            friendly_name='Unit Test Category',
            description='unit test description',
        )
        self.assertEqual(
            category.get_friendly_name(), category.friendly_name
        )

    def test_product_str(self):
        """
        Tests if Product model str method returns correct string
        """
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        self.assertEqual(product.__str__(), product.name)
