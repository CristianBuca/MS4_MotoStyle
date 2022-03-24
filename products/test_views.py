# Imports
# 3rd party:
from django.test import TestCase
# -----------------------------------------------------------------------------
# Create your tests here.

class TestProductsViews(TestCase):
    """
    Defines the views unit tests for the products app
    """
    def test_get_products(self):
        