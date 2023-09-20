from django.urls import path
from . import views
from .views import TicketUpdateView,TicketDetailView,TicketListView

urlpatterns = [
    path('create/', views.CreateTicket, name='create-ticket'),
    path('tickets/', views.DisplayTicket, name='tickets'),
    path('tickets/<int:pk>/update/', TicketUpdateView.as_view(), name='update-ticket')
]