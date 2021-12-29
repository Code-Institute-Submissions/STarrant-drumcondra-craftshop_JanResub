# products/models

from django.db import models

# Create your models here.


# Product Category Model
class Category(models.Model):

    # Code Credit:  'Categorys' Spelling fix courtesy of Chris Z (https://github.com/ckz8780)
    class Meta:
        ''' Meta class to show plural of Category in admin. '''
        verbose_name_plural = 'Categories'

    category_tag = models.CharField(max_length=254)
    category_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        ''' Return the category tag name. '''
        return self.category_tag

    def get_category_name(self):
        ''' Return the verbose version of the category name in admin. '''
        return self.category_name


# Creators Model
class Creator(models.Model):
    ''' Creator Model '''
    name = models.CharField(max_length=254)
    bio = models.TextField(max_length=10000)
    img_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        ''' Return the creator name. '''
        return self.name


# Item Model
class Item(models.Model):
    ''' Item Model '''
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=10000)
    category_id = models.ForeignKey('Category', null=True, blank=True,
                                    on_delete=models.SET_NULL)
    creator_id = models.ForeignKey('Creator', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    unitcost = models.DecimalField(max_digits=6, decimal_places=2)
    weight_g = models.DecimalField(max_digits=6, decimal_places=0)
    ship_in_packet = models.BooleanField(default=False)
    img_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        ''' Return the item name. '''
        return self.name


# Products Model
class Product(models.Model):
    ''' Product model '''
    item_id = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
    )
    sku = models.CharField(max_length=254, blank=True)
    salesmargin = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    stockcount = models.DecimalField(max_digits=6, decimal_places=0,
                                     null=True, blank=True)

    def __str__(self):
        ''' Return the product name. '''
        return self.item_id.name

    def _get_unit_price(self):
        """Returns the calculated unit cost of the product"""
        return self.item_id.unitcost * (1 + self.salesmargin)
    unit_price = property(_get_unit_price)
