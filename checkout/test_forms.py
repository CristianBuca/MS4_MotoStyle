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
        trying to submit form with empty name field
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
