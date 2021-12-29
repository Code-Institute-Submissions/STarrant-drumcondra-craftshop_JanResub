# checkout/views.py

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderLineItem

# Create your views here.


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your shopping basket is empty.")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_live_51JtLsMCzvnOhwero3k5nYnyBD8U4kGY2tn0yEQaI5EKcCGgmzN4pU63dq3FQntS7PmIMjgfyA9gDH8HJOLJfP8a200xy55ihKq',
        'client_secret': 'client secret test value',
    }

    return render(request, template, context)
