# Imports
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
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
        blank_label='Country', null=True, blank=True
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Receiver for post_save event from the user model.
    Creates user profile or updates it if already exists.
        Arguments:
            sender (object): The user sending the request
            instance (object): The instance of the object
            created (object): The flag to create a new user in DB
            **kwargs (object): keyword arguments
        Returns: N/A
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
