# checkout/views.py

import json

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

import stripe

from basket.contexts import basket_contents
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Item, Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

# Create your views here.


@require_POST
def cache_checkout_data(request):
    """
    Caching checkout data.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Sorry. Your payment cannot be processed now.\
                       Please try again later.")
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_no': request.POST['phone_no'],
            'address_street_1': request.POST['address_street_1'],
            'address_street_2': request.POST['address_street_2'],
            'address_town_city': request.POST['address_town_city'],
            'address_postcode': request.POST['address_postcode'],
            'address_country': request.POST['address_country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
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
                        "One of the products in your shopping \
                            basket does not exist in our database."
                        "Please contact us for assistance."}
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_no]))
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

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_no': profile.default_phone_no,
                    'address_street_1': profile.default_address_street_1,
                    'address_street_2': profile.default_address_street_2,
                    'address_town_city': profile.default_address_town_city,
                    'address_postcode': profile.default_address_postcode,
                    'address_country': profile.default_address_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
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


def checkout_success(request, order_no):
    """
    Renders the follow page on completion of a successful order.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_no=order_no)

    profile = UserProfile.objects.get(user=request.user)
    order.user_profile = profile
    order.save()

    if save_info:
        profile_data = {
            'default_email': order.email,
            'default_phone_no': order.phone_no,
            'default_address_street_1': order.address_street_1,
            'default_address_street_2': order.address_street_2,
            'default_address_town_city': order.address_town_city,
            'default_address_postcode': order.address_postcode,
            'default_address_country': order.address_country,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Thank you for your order. \
        Your order number is { order_no }. \
        A confirmation email will be sent to { order.email }.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html/'
    context = {
        'order': order,
    }

    return render(request, template, context)
