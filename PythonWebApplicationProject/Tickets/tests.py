from django.test import TestCase
from .models import Ticket
from django.urls import reverse

# Create your tests here.
class TicketTest(TestCase):

    def test_create(self):
        ticket_data = {
            'Title' : 'Test Input',
            'Problem' : 'This is a test problem',
            'Status' : 'Major',
        }


        #Post ticket is sent to the server 
        response = self.client.post(reverse('create'), ticket_data, follow=True)

        #This checks to see if the response was successful, using the HTTPS response 200 which is a succesful response status code    
        self.assertEqual(response.status_code, 200)
        
    def test_update(self):
        ticket = Ticket.objects.create(Title='Ticket update', Problem='Ticket problem', Status='Minor')
        
        
        update_data = {
            'Title': 'Updated title',
            'Problem': 'Updated problem description',
            'Status': 'Critical',
        }
        
        
        response = self.client.post(reverse('update-ticket', args=[ticket.id]), update_data, follow=True)
        
        self.assertEqual(response.status_code, 200)
        
    def test_sql_inject(self):
        
        #Malicious sql input to simulate an injection attack through a malicious query
        sql_injection_input = "admin' OR '1'=1"
        ticket_vuln = Ticket.objects.create(Title=sql_injection_input, Problem = 'test inject', Status='Critical')
        
        #Saves the ticket which should not raise an error or exception
        ticket_vuln.save()
        
        #Verifies that the injection attack hasn't affected the database. 
        self.assertTrue(Ticket.objects.filter(title=sql_injection_input))