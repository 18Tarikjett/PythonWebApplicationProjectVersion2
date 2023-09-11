from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# The Ticket form can inherit from the User form for its foreign key, but must use it's own custom written variables.


class Ticket(models.Model):
     TicketTitle = models.CharField(max_length=250)
     TicketProblem = models.TextField()
     TicketCreationDate = models.DateTimeField(auto_now_add=True)
     TicketUpdatedDate =  models.DateTimeField(auto_now=True)
     TicketStatus = models.CharField(max_length=20, default='Minor')
     user = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
          return self.title 