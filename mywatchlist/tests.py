from django.test import TestCase

# Create your tests here.
from multiprocessing.connection import Client
from django.test import TestCase, Client
from django.urls import reverse

class test(TestCase):
    def testHtml(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_watchlist"))
        self.assertEquals(response.status_code,200)

    def testJSON(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_json"))
        self.assertEquals(response.status_code,200)

    def testXML(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_xml"))
        self.assertEquals(response.status_code,200)