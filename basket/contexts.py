# basket/context.py

from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):
    """ Context processor for shopping basket. """

    basket_items_list = []
    total_value = 0
    item_count = 0
    unit_price = 0.00
    line_value = 0.00

    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        unit_price = product.item_id.unitcost * (1 + product.salesmargin)
        line_value = quantity * unit_price
        total_value += line_value
        item_count += quantity
        basket_items_list.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'unit_price': unit_price,
            'line_value': line_value,
        })

    context = {
        "basket_items_list": basket_items_list,
        "total_value": total_value,
        "item_count": item_count,
        "delivery_cost": "TBA",
        "grand_total": "TBA",
    }

    return context
