# Imports
# 3rd party:
from django import template
# -----------------------------------------------------------------------------


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Custom django filter to calculate subtotal for items in cart
        Arguments:
            price: the price of each item
            quantity: the quantity of each item
        Returns:
            the subtotal for each item
    """
    return price * quantity
