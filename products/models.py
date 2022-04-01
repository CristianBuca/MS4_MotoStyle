# Imports
# 3rd party:
from django.db import models
# -----------------------------------------------------------------------------


class Category(models.Model):
    """
    Class defining the fields in Category model
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        """
        Returns the category name string
            Arguments: self (object): self
            Returns: Category name as string
        """
        return str(self.name)

    def get_friendly_name(self):
        """
        Returns the category friendly name string
            Arguments: self (object): self
            Returns: Category friendly name as string
        """
        return self.friendly_name


class Product(models.Model):
    """
    Class defining the fields in Product model
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    new_rating = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, blank=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        """
        Returns the category name string
            Arguments: self (object): self
            Returns: Category name as string
        """
        return str(self.name)
