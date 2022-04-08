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

