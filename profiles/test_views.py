# Imports
# 3rd Party:
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
# Internal
from checkout.models import Order
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

    def test_get_order_history(self):
        """
        Tests if user can access the order page with status code 200
        Tests if toast displays correct message
        """
        user = User.objects.create_user(
            username='unit_test_user', password='unit_test_pass'
        )
        order = Order.objects.create(
            order_number='11111111',
            full_name='Unit Test',
            email='unit_test@motostyle.com',
            phone_number='1111111111',
            country='GB',
            postcode='11111',
            town_or_city='Unit test city',
            address_line1='Unit test address',
            area='Unit test area',
            user_profile_id=user.id,
        )
        self.client.login(username='unit_test_user', password='unit_test_pass')
        response = self.client.get(
            f'/profile/order_history/{order.order_number}'
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            str(messages[0]),
            f'This is a past confirmation for order '
            f'number {order.order_number}. '
            'A confirmation email was sent at the time the order was placed'
        )
