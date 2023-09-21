from django.db import models
from django.forms.models import BaseModelForm
from django.utils import timezone
from django.shortcuts import render,redirect
from django.contrib import messages
from django import forms
from django.http import Http404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic import (
    UpdateView,
    ListView,
    DetailView,
    DeleteView
    )
from .forms import TicketCreationForm
from .models import Ticket

# Create your views here.

# This ticket view imports from forms, which then imports from ticket class.
# The Ticket view has Create and Display ticket functions which utilize the ticket class form, as data is being inputted which forms handle. 
# Updating a ticket or deleting however, is mainly implemented within the views.py file in django


@login_required
def CreateTicket(request):
    if request.method == 'POST':
        ticket_form = TicketCreationForm(request.POST, user=request.user)
        if ticket_form.is_valid():
            ticket_form.save()
            ticket_form.user = request.user
            ticket = ticket_form.save()
            messages.success(request, f'{ticket} has been created.')
            return redirect('../tickets/', pk=ticket.pk)    
    else:
        ticket_form = TicketCreationForm()
    return render(request, 'create_ticket.html', {'form' : ticket_form})


@login_required
def DisplayTicket(request):
        ticket_display = Ticket.objects.filter(user=request.user)
        return render(request, 'display_ticket.html', {'tickets' : ticket_display})



class TicketListView(ListView):
    model = Ticket
    template_name = 'HelpDeskProject/home.html'
    context_object_name = 'ticket'
    ordering = ['-date-posted']



class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'



#The TicketUpdateViw class utilizes the LoginRequiredMixin, UserPassesTestMixin as authentication mixins and UpdateView as a django view. 

class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket 
    fields = ['Title', 'Problem', 'Status']
    template_name = 'update_ticket.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #The Ticket should only be able to be updated by the user that created the ticket. 
    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.user:
            return True
        else:
            return False


class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    
    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.user:
            return True
        else:
            return False
