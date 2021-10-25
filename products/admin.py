# products/admin.py

from django.contrib import admin
from .models import Product, Item, Category, Creator

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """
    A class that extends the ModelAdmin class.
    Tells the Admin which product fields to display.
    """
    list_display = (
        'item_id',
        'sku',
        'salesmargin',
        'rating',
        'stockcount',
    )

    ordering = ('sku',)


class ItemAdmin(admin.ModelAdmin):
    """
    A class that extends the ModelAdmin class.
    Tells the Admin which Item fields to display.
    """
    list_display = (
        'name',
        'image',
        'category_id',
        'creator_id',
        'unitcost',
        'weight_g',
        'ship_in_packet',
    )


class CategoryAdmin(admin.ModelAdmin):
    """
    A class that extends the ModelAdmin class.
    Tells the Admin which category fields to display.
    """
    list_display = (
        'category_name',
        'category_tag',
    )


class CreatorAdmin(admin.ModelAdmin):
    """
    A class that extends the ModelAdmin class.
    Tells the Admin which creator fields to display.
    """
    list_display = (
        'name',
        'bio',
        'image',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Creator, CreatorAdmin)
