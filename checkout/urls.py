# checkout/urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('shipping', views.checkout, name='shipping'),
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_no>', views.checkout_success, name='checkout_success'),
]
