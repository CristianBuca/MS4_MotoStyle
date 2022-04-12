# Imports
# 3rd party:
from django.test import TestCase
# -----------------------------------------------------------------------------


class TestHomeViews(TestCase):
    """
    Class defining the views tests for the home app
    """
    def test_get_home_page(self):
        """
        Test if the home page is accessible with a status code of 200
        Test if the the template rendered is 'index.html'
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
