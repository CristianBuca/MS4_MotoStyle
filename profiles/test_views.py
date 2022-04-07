# Imports
# 3rd Party:
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
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

    def test_post_profile(self):
        """
        Tests if user can edit their delivery information
        Tests if correct message is displayed in toast
        """
        user = User.objects.create_user(
            username='unit_test_user', password='unit_test_pass'
        )
        self.client.login(username='unit_test_user', password='unit_test_pass')
        response = self.client.post('/profile/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(messages[0]), 'Profile updated successfully')
