# participant_records/urls.py
from django.urls import path
from .views import participant_records_view

urlpatterns = [
    path('', participant_records_view, name='participant_records'),
]
