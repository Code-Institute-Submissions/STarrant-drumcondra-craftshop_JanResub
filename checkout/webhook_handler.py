from django.http import HttpResponse


class StripeWH_Handler:
    """Handler class for Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle an unexpected webhook event
        """
        print('Webhook_handler.py - unexpected event')  # testhigh
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment intent succeeded webhook from Stripe
        """
        intent = event.data.object
        print('Webhook_handler.py - intent succeeded')  # testhigh
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Handle the payment intent failed webhook from Stripe
        """
        print('Webhook_handler.py - intent failed')  # testhigh
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
