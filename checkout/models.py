# checkout/models.py
import uuid

from django.db import models
from django.db.models import Sum
from django.contrib.postgres.aggregates import BoolAnd
from django.conf import settings
from django_countries.fields import CountryField

from products.models import Product, Item


class Order(models.Model):
    order_no = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_no = models.CharField(max_length=20, null=False, blank=False)
    address_street_1 = models.CharField(max_length=80, null=False, blank=False)
    address_street_2 = models.CharField(max_length=80, null=True, blank=True)
    address_town_city = models.CharField(max_length=40, null=False, blank=False)    
    address_postcode = models.CharField(max_length=20, null=True, blank=True)
    address_country = CountryField(null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    order_weight_g = models.IntegerField(null=False, default=0)
    order_items_ship_in_packet = models.BooleanField(default=False)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_no(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        update the order_items_ship_in_packet flag to ensure
        all items will ship in a single packet,
        update the total order_weight_g with the weight of
        the new line item,
        recalculate the delivery cost.
        """
        self.order_total = self.lineitems.aggregate(Sum(
            'lineitem_total'))['lineitem_total__sum'] or 0
        self.order_weight_g = self.lineitems.aggregate(Sum(
            'lineitem_weight_g'))['lineitem_weight_g__sum'] or 0
        # Source for use of aggregate(BoolAnd)
        # https://django.readthedocs.io/en/stable/ref/contrib/postgres/aggregates.html
        self.order_items_ship_in_packet = False # testhigh
        # self.order_items_ship_in_packet = self.lineitems.aggregate(BoolAnd('lineitem_ship_in_packet'))['lineitem_ship_in_packet'] or False
        self.delivery_cost = 0  # calculation for delivery cost to be added testhigh
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_no:
            self.order_no = self._generate_order_no()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_no


class OrderLineItem(models.Model):
    order = models.ForeignKey(
                Order,
                null=False,
                blank=False,
                on_delete=models.CASCADE,
                related_name='lineitems'
                )
    product = models.ForeignKey(
                Product,
                null=False,
                blank=False,
                on_delete=models.CASCADE
                )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
                max_digits=6,
                decimal_places=2,
                null=False,
                blank=False,
                editable=False
                )
    lineitem_weight_g = models.IntegerField(null=False, blank=False)
    lineitem_ship_in_packet = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = (self.product.item_id.unitcost *
                               self.product.salesmargin *
                               self.quantity)
        self.lineitem_weight_g = (self.product.item_id.weight_g)
        self.lineitem_ship_in_packet = (self.product.item_id.ship_in_packet)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_no}'


class ShippingZone(models.Model):
    """
    ShippingZone model contains the main data fields to allow a shipping
    calculation of An Post (Irish Postal Service) shipping costs.
    There are five shipping zones - Ireland, UK, EU, AU/NZ and Rest of World.
    There are two package sizes and associated rates, packet and parcel.
    Both package and parcel have limits to shipping weights.
    """
    shipping_zone_no = models.IntegerField(null=False, blank=False, default=0)
    shipping_zone_name = models.IntegerField(null=False, blank=False, default=0)
    country_list = models.CharField(max_length=80, null=False, blank=False)
    packet_limit_g = models.IntegerField(null=False, blank=False, default=0)
    parcel_limit_g = models.IntegerField(null=False, blank=False, default=0)
    parcel_excess_limit_g = models.IntegerField(null=False, blank=False, default=0)
    parcel_excess_rate = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_excess_basecost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    packet_cost_00100g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    packet_cost_00250g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    packet_cost_00500g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    packet_cost_01000g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    packet_cost_01500g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    packet_cost_02000g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_00100g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_00250g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_00500g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_01000g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_01500g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_02000g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_02500g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_03000g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_03500g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_04000g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_04500g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_05000g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_15000g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    parcel_cost_20000g = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)

    def __str__(self):
        return f'SKU {self.shipping_zone_name}'
