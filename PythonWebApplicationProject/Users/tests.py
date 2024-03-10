from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.
class URLTests(TestCase):
    def test_loginpage(self):
        response = self.client.get('/login')
        self.assertEqual(response.request, 200)

    def test_logoutpage(self):
        response = self.client.get('/logout')
        self.assertEqual(response.request, 200)
        
    def user_setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='RandomUser', password='testpass')
        
    def tearDown(self):
        self.user.delete()
    
    def test_unauthorised_user(self):
        response = self.client.get(reverse('views'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/Users/views/login')
        
    def test_authorised_user(self):
        self.client.login(username='RandomUser', password='testpass')
        
        response = self.client.get(reverse('views'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
    