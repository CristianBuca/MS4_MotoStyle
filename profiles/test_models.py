# Imports
# 3rd party:
from django.test import TestCase
# -----------------------------------------------------------------------------


class TestProfileModels(TestCase):
    """
    Defines the models unit tests for the profile app
    """

    def test_profile_str(self):
        """
        Tests if UserProfile model str method returns correct string
        """
        