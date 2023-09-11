from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateTicket, name='Ticket'),
    # path('ticket/<int:pk>', views.display_ticket, name='display_ticket')
]