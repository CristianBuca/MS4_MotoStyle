# Imports
# 3rd Party
from django.http import HttpResponse
# -----------------------------------------------------------------------------


class StripeWH_Handler:
    """
    Class with the methods required to handle the stripe webhook
    """

    def __init__(self, request):
        """
        Handler initialization.
            Arguments:
                self (object): The object init
                request (object): The request object
            Returns: Request
        """
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event from stripe
            Arguments:
                self(object): the event object
                event: the event
            Return: HttpResponse 200
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
            Arguments:
                self(object): the event object
                event: the event
            Return: HttpResponse 200
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
            Arguments:
                self(object): the event object
                event: the event
            Return: HttpResponse 200
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
