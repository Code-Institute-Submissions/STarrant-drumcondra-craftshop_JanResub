from django.test import TestCase
from .models import Product

# Create your tests here.

class ProductDetailPageTest(TestCase):
    """ Test for products page response. """
    def setUp(self):
        Product.objects.create(name='test_product', price='1.00')
    
    def test_product_creation(self):
        product=Product.objects.get(id=1)
        expected_object_name = f'(product.name)'
        self.assertEqual(expected_object_name, 'test_product')
