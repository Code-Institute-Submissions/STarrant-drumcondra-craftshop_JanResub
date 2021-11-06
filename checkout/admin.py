# checkout/admin.py

from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)

    readonly_fields = ('order_no', 'order_date', 'order_weight_g',
                       'order_items_ship_in_packet', 'delivery_cost',
                       'order_total', 'grand_total',)

    fields = ('order_no', 'order_date', 'full_name', 'email', 
              'phone_no', 'address_street_1', 'address_street_2',
              'address_town_city', 'address_postcode', 'address_country',
              'order_weight_g', 'order_items_ship_in_packet',
              'order_total', 'delivery_cost', 'grand_total')

    list_display = ('order_no', 'order_date', 'full_name', 'email',
                    'order_weight_g', 'order_items_ship_in_packet',
                    'order_total', 'delivery_cost', 'grand_total')


admin.site.register(Order, OrderAdmin)
