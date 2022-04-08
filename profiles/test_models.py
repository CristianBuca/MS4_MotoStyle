# Imports
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
# Internal
from .models import UserProfile
# -----------------------------------------------------------------------------


class TestProfileModels(TestCase):
    """
    Defines the models unit tests for the profile app
    """

    def test_profile_str(self):
        """
        Tests if UserProfile model str method returns correct string
        """
        user = User.objects.create_user(
            username='unit_test',
            password='test_pass',
            email='test@unittest.com',
        )
        user_profile = UserProfile.objects.get(user=user)
        self.assertEqual(str(user_profile), user_profile.user.username)
