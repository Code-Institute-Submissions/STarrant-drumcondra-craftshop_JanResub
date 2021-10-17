from django.test import TestCase

# Create your tests here.

# url response tests

class HomePageTest(TestCase):
    """ Test for homepage response. """
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class ProductPageTest(TestCase):
    """ Test for products page response. """
    def test_home_page_status_code(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
