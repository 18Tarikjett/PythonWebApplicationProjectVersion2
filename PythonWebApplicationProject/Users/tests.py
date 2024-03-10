from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch


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
        
        
    def tearDown(self):
        self.user.delete()
    
    def test_unauthorised_user(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/Users/views/register')
    
    #The patch decorator means that a mock authentication is used for a mock user instead of a real one.
    @patch('django.contrib.auth.authenticate')    
    def test_authorised_user(self):
        #Mock authenticate returns a mock or fake user object. This means that even fake users don't exist within the code.
        mock_user = mock.authenticate.return_value
        mock_user.is_authenticated = True
        
        response = self.client.get(reverse('profile'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
    