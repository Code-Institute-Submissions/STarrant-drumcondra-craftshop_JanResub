from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

# Code Credit:  Chris Z. (https://github.com/ckz8780)
# Boutique Ado Project used as the basis for code below.

def profile(request):
    '''
    Display user's profile page.
    '''
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_no):
    '''
    view to create order history.
    '''
    order = get_object_or_404(Order, order_no=order_no)

    messages.info(request, (
        f'This is a history confirmation for order number, {order_no}.\
            A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, template, context)
