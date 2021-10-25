from django.test import TestCase
from .models import Category, Product, Creator, Item

# Create your tests here.


class TestModels(TestCase):

    def test_category_string_method_returns_name(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(str(category), 'Test Category')


    def test_product_string_method_returns_name(self):
        product = Product.objects.create(name='Test Product', price=1.00)
        self.assertEqual(str(product), 'Test Product')

    def test_creator_string_method_returns_name(self):
        creator = Creator.objects.create(name='Test Creator')
        self.assertEqual(str(creator), 'Test Creator')