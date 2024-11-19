# myproject/urls.py
from django.contrib import admin
from django.urls import include, path
from .views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/', include('event_management.urls')),  # Event management app
    path('participants/', include('participant_records.urls')),  # Participant records app
    path('auth/', include('user_auth.urls')),  # User auth app
    path('volunteer/', include('volunteer_management.urls')),  # Volunteer management app
    path('',welcome, name='welcome'),
    

]