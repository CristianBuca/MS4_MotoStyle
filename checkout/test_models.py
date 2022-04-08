# Imports
# 3rd party:
from django.test import TestCase
# Internal
from .models import Order
# -----------------------------------------------------------------------------


class TestCheckoutModels(TestCase):
    """
    Defines the models unit test for the checkout app
    """
    def test_order_model(self):
        """
        Tests if order model returns correct string
        """
        Order.objects.create(
            full_name='test user',
            email='test@unittest.com',
            phone_number='1234567890',
            address_line1='test address line',
            town_or_city='test city',
            country='US',
        )
        order = Order.objects.get(email='test@unittest.com')
        self.assertEqual(str(order), order.order_number)
