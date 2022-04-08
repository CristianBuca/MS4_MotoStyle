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
        Category.objects.create(
            name='unit_test_category',
            friendly_name='Unit Test Category',
            description='unit test description',
        )
        category = Category.objects.get(name='unit_test_category')
        self.assertEqual((category.__str__()), category.name)

    def test_category_friendly(self):
        """
        Tests if Category model get_friendly_name returns correct string
        """
        Category.objects.create(
            name='unit_test_category',
            friendly_name='Unit Test Category',
            description='unit test description',
        )
        category = Category.objects.get(name='unit_test_category')
        self.assertEqual((
            category.get_friendly_name()), category.friendly_name
        )
