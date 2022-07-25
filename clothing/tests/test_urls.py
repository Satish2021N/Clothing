from django.urls import reverse, resolve
from django.test import SimpleTestCase
from clothing.views import home, sign_up, about, collections, productview

from django.test import SimpleTestCase

class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
    
    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)
    
    def test_sign_up_url_resolves(self):
        url = reverse('sign_up')
        self.assertEquals(resolve(url).func, sign_up)
    
    def test_collections_url_resolves(self):
        url = reverse('collections')
        self.assertEquals(resolve(url).func, collections)
        