# Imports
# 3rd party:
from django.test import TestCase
# Internal
from .forms import UserProfileForm
# -----------------------------------------------------------------------------


class TestProfilesForms(TestCase):
    """
    Defines the forms unit tests for the profiles app
    """

    def test_profiles_form_update(self):
        """
        Tests if profile form updates upon submission
        """
        form = UserProfileForm({
            'default_full_name': 'Unit Test Name',
            'default_email': 'test@unittest.com',
            'default_phone_number': '1234567890',
            'default_address_line1': 'Test address 1',
            'default_address_line2': 'Test address 2',
            'default_town_or_city': 'Town',
            'default_postcode': '12345',
            'default_area': 'Test Area',
        })
        self.assertTrue(form.is_valid())
