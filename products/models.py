# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models


class Category(models.Model):
    """
    Class defining the fields in Category model
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        Returns the category name string
            Arguments: self (object): self
            Returns: Category name as string
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the category friendly name string
            Arguments: self (object): self
            Returns: Category friendly name as string
        """
        return self.friendly_name
