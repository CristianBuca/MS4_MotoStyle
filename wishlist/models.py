# Imports
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
# Internal
from products.models import Product
# -----------------------------------------------------------------------------


class Wishlist(models.Model):
    """
    Defines the Favorites model
    """

    products = models.ManyToManyField(Product, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the name of the wishlist as a string
            Arguments: self (object): The wishlist object
            Return: The wishlist's name as string
        """
        return f"{self.owner}'s Wishlist"
