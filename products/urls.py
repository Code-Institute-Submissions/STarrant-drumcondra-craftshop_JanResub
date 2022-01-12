# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit_item/<int:item_id>', views.edit_item, name='edit_item'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>', views.edit_product, name='edit_product'),
]
