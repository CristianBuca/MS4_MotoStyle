# Imports
# 3rd party:
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Internal
from .models import OrderLineItem
# -----------------------------------------------------------------------------


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Handles signals from post_save events to update order:
        Arguments:
            sender (object): OrderLineItem object
            instance: Instance of the model that sent it
            created: Boolean signaling if created or updated
            **kwargs: key word arguments
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, created, **kwargs):
    """
    Handles signals from post_delete events to update order:
        Arguments:
            sender (object): OrderLineItem object
            instance: Instance of the model that sent it
            **kwargs: key word arguments
    """
    instance.order.update_total()
