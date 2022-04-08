# Imports
# 3rd party:
from django.test import TestCase
# Internal
from .forms import ProductForm
# -----------------------------------------------------------------------------


class TestProductsForms(TestCase):
    """
    Defines the forms unit tests for the products app
    """

    def test_product_form_no_name(self):
        """
        Tests if correct error is displayed to the user when
        trying to submit form with empty name field
        Tests if form fails validation
        """
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(
            form.errors['name'][0], 'This field is required.'
        )

    def test_product_form_no_price(self):
        """
        Tests if correct error is displayed to the user when
        trying to submit form with empty price field
        Tests if form fails validation
        """
        form = ProductForm({
            'name': 'Unit Test Product',
            'price': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(
            form.errors['price'][0], 'This field is required.'
        )

    def test_product_form_no_decription(self):
        """
        Tests if correct error is displayed to the user when
        trying to submit form with empty description field
        Tests if form fails validation
        """
        form = ProductForm({
            'name': 'Unit Test Product',
            'price': '123.45',
            'description': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0], 'This field is required.'
        )

    def test_product_form_is_valid(self):
        """
        Test if form validates correctly when all fields are filled in
        """
        form = ProductForm({
            'name': 'Unit Test Product',
            'price': '123.45',
            'description': 'Unit test product description'
        })
        self.assertTrue(form.is_valid())
