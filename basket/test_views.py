from django.test import TestCase

# Create your tests here.

# url response tests

class BasketPageTest(TestCase):
    """ Test for basket page response. """
    def test_basket_page_status_code(self):
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
