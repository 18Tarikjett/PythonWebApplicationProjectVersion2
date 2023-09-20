from django.test import TestCase

# Create your tests here.

class URLTests(TestCase):
    def test_homepage(self):
        response = self.client.get('')
        self.assertEqual(response.request, 200)

    def test_aboutage(self):
        response = self.client.get('/about')
        self.assertEqual(response.request, 200)

    def test_loginpage(self):
        response = self.client.get('/login')
        self.assertEqual(response.request, 200)

    def test_logoutpage(self):
        response = self.client.get('/logout')
        self.assertEqual(response.request, 200)