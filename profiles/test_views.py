# Imports
# 3rd Party:
from django.test import TestCase
from django.contrib.auth.models import User
# -----------------------------------------------------------------------------


class TestProfileViews(TestCase):
    """
    Defines the views unit tests for the profiles app
    """
    def test_get_profile(self):
        """
        Tests if profile page is accessible to the user with status 200
        Tests if view renders the profile.html template
        """
        user = User.objects.create_user(
            username='unit_test_user', password='unit_test_pass'
        )
        self.client.login(username='unit_test_user', password='unit_test_pass')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
