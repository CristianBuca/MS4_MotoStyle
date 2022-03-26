# Imports
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
# Internal
from products.models import Product
# -----------------------------------------------------------------------------


class Wishlist(models.Model):
    """
    Defines the Wishlist model
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

    def __str__(self):
        """
        Returns the name of the wishlist as a string
            Arguments: self (object): The wishlist object
            Return: The wishlist's name as string
        """
        return f"{self.owner}'s Wishlist"
