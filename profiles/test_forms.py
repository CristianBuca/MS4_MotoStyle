# Imports
# 3rd party:
from django.test import TestCase
# -----------------------------------------------------------------------------


class TestProfilesForms(TestCase):
    """
    Defines the forms unit tests for the profiles app
    """

    def test_profiles_form_update(self):
        """
        Tests if profile form updates upon submission
        """
        