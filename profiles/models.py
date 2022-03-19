# Imports
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# -----------------------------------------------------------------------------


class UserProfile(models.Model):
    """
    Class to give the user the ability to store default delivery information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=50, null=True, blank=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_address_line1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_address_line2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
    )
    default_area = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country *', null=True, blank=True
    )
