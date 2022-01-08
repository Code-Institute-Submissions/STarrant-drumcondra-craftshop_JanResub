# checkout/views.py

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
import stripe

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Item, Product
from basket.contexts import basket_contents

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST('full_name'),
            'email': request.POST('email'),
            'phone_no': request.POST('phone_no'),
            'address_street_1': request.POST('address_street_1'),
            'address_street_2': request.POST('address_street_2'),
            'address_town_city': request.POST('address_town_city'),    
            'address_postcode': request.POST('address_postcode'),
            'address_country': request.POST('address_country'),
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, {
                        "One of the products in your shopping basket does not exist in our database."
                        "Please contact us for assistance."}
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "Your shopping basket is empty.")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key missing.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
