from django.conf import settings

def basket_contents(request):
    """ Context processor for shopping basket. """

    basket_items_list = []
    total_value = 0
    item_count = 0

    context = {
        "basket_items_list": basket_items_list,
        "total_value": total_value,
        "item_count": item_count,
    }

    return context
