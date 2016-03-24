from django.core.urlresolvers import resolve
from django.test import TestCase
from home.views import home_page

# Create your tests here.

class HomePageTest(TestCase):
    def test_home_page_url_using_correct_function(self):
        url = resolve('/')
        self.assertEqual(url.func, home_page)