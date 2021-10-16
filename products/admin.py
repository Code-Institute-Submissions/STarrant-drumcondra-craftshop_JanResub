# products/admin.py

from django.contrib import admin
from .models import Product, Category, Creator

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """
    A class that extends the ModelAdmin class.
    Tells the Admin which product fields to display.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'creator',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    A class that extends the ModelAdmin class.
    Tells the Admin which category fields to display.
    """
    list_display = (
        'friendly_name',
        'name',
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
admin.site.register(Category, CategoryAdmin)
admin.site.register(Creator, CreatorAdmin)
