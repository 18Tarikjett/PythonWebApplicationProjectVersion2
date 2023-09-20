from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import Ticket
from django.utils import timezone


critical_level = [
    ('MIN','Minor'),
    ('MAJ','Major'),
    ('CRIT','Critical'),
    ('RES', 'resolved')
]

class TicketCreationForm(forms.ModelForm):
     class Meta:
         model = Ticket
         fields = [ 'Title','Problem','Status']
     
     def __init__(self, *args, **kwargs):
          user = kwargs.pop('user', None)
          super(TicketCreationForm, self).__init__(*args, **kwargs)
          self.instance.user = user
