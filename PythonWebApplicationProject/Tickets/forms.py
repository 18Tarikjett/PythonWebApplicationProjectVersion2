from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import Ticket
from django.utils import timezone


critical_level = [
    ('MIN','Minor'),
    ('MAJ','Major'),
    ('CRIT','Critical'),
]

class TicketCreationForm(forms.ModelForm):
     class Meta:
         model = Ticket
         fields = [ 'TicketTitle','TicketProblem']
    


