from django.db import models
from django.utils import timezone
from django.shortcuts import render,redirect 
from django.contrib import messages
from django import forms
from .forms import TicketCreationForm

# Create your views here.

def CreateTicket(request):
    if request.method == 'POST':
        ticket_form = TicketCreationForm(request.POST)
        if ticket_form.is_valid():
            ticket_form.save()
            ticket = ticket_form.save()
            messages.success(request, f'{ticket} has been created.')
            return redirect('display_ticket', pk=ticket.pk)
    else:
        ticket_form = TicketCreationForm()
    return render(request, 'create_ticket.html', {'form' : ticket_form})


