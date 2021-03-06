# Imports
# 3rd party:
from django.test import TestCase
# Internal:
from .forms import OrderForm
# -----------------------------------------------------------------------------


class TestsCheckoutForms(TestCase):
    """
    Defines the forms unit tests for the checkout app
    """

    def test_order_form_no_name(self):
        """
        Tests if correct error is displayed to the user when
        trying to submit form with empty name field
        Tests if form fails validation
        """
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.'
        )

    def test_order_form_no_email(self):
        """
        Tests if correct error is displayed to the user when
        trying to submit form with empty email field
        Tests if form fails validation
        """
        form = OrderForm({
            'full_name': 'test user',
            'email': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.'
        )

    def test_order_form_no_phone(self):
        """
        Tests if correct error is displayed to the user when
        trying to submit form with empty phone number field
        Tests if form fails validation
        """
        form = OrderForm({
            'full_name': 'test user',
            'email': 'test@unittest.com',
            'phone_number': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.'
        )

    def test_order_form_no_address(self):
        """
        Tests if correct error is displayed to the user when
        trying to submit form with empty address line field
        Tests if form fails validation
        """
        form = OrderForm({
            'full_name': 'test user',
            'email': 'test@unittest.com',
            'phone_number': '1234567890',
            'address_line1': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('address_line1', form.errors.keys())
        self.assertEqual(
            form.errors['address_line1'][0], 'This field is required.'
        )

    def test_order_form_no_city(self):
        """
        Tests if correct error is displayed to the user when
        trying to submit form with empty city line field
        Tests if form fails validation
        """
        form = OrderForm({
            'full_name': 'test user',
            'email': 'test@unittest.com',
            'phone_number': '1234567890',
            'address_line1': 'test address line',
            'town_or_city': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.'
        )

    def test_order_form_no_country(self):
        """
        Tests if correct error is displayed to the user when
        trying to submit form with no country selected
        Tests if form fails validation
        """
        form = OrderForm({
            'full_name': 'test user',
            'email': 'test@unittest.com',
            'phone_number': '1234567890',
            'address_line1': 'test address line',
            'town_or_city': 'test city',
            'country': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
            form.errors['country'][0], 'This field is required.'
        )

    def test_order_form_valid(self):
        """
        Test if form validates correctly when all fields are filled in
        """
        form = OrderForm({
            'full_name': 'test user',
            'email': 'test@unittest.com',
            'phone_number': '1234567890',
            'address_line1': 'test address line',
            'town_or_city': 'test city',
            'country': 'US',
        })
        self.assertTrue(form.is_valid())
