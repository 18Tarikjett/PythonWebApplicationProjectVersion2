from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Permission
from django.urls import reverse

# Create your models here.
# The Ticket form can inherit from the User form for its foreign key, but must use it's own custom written variables.


class Ticket(models.Model):
     Title = models.CharField(max_length=250)
     Problem = models.TextField()
     TicketCreationDate = models.DateTimeField(auto_now_add=True)
     TicketUpdatedDate =  models.DateTimeField(auto_now=True)
     Status = models.CharField(max_length=20, default='Minor')
     user = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
          return self.Title
     
     def get_absolute_url(self):
          return reverse('ticket-detail', kwargs={'pk': self.pk})
