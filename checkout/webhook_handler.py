import json
import time

from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile


class StripeWH_Handler:
    """Handler class for Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle an unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment intent succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Replace blank fields from Stripe with None values
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update Profile Information when save info is checked.
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            profile.default_phone_no = shipping_details.phone_no
            profile.default_address_country = shipping_details.country
            profile.default_address_postcode = shipping_details.postal_code
            profile.default_address_town_city = shipping_details.city
            profile.default_address_street_1 = shipping_details.line1
            profile.default_address_street_2 = shipping_details.line2
            profile.save()

        order_exists = False
        attempt = 1
        # Check if order exists 5 times - break if found.
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=shipping_details.email,
                    phone_no__iexact=shipping_details.phone_no,
                    address_country__iexact=shipping_details.country,
                    address_postcode__iexact=shipping_details.postal_code,
                    address_town_city__iexact=shipping_details.city,
                    address_street_1__iexact=shipping_details.line1,
                    address_street_2__iexact=shipping_details.line2,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        # If order exists - exit success.
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | \
                SUCCESS: Order verified and already in database.',
                status=200)
        # Else Order does not exist - create order from Stripe webhook data.
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_no=shipping_details.phone_no,
                    address_country=shipping_details.address.country,
                    address_postcode=shipping_details.address.postal_code,
                    address_town_city=shipping_details.address.city,
                    address_street_1=shipping_details.address.line1,
                    address_street_2=shipping_details.address.line2,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        # Code succeeded in creating an order - Exit Success.
        return HttpResponse(
            content=f'Webhook received: {event["type"]} |\
            SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Handle the payment intent failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
