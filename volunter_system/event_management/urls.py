# event_management/urls.py
from django.urls import path
from .views import event_list
from .views import add_event, edit_event, delete_event,organizer_dashboard

urlpatterns = [
    path('', event_list, name='event_li'),
    path('add/', add_event, name='add_event'),
    path('edit/<int:event_id>/', edit_event, name='edit_event'),
    path('delete/<int:event_id>/', delete_event, name='delete_event'),
    path('organizer/', organizer_dashboard, name='organizer_dashboard'),

]