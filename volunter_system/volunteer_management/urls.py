# volunteer_management/urls.py
from django.urls import path
from .views import event_details,event_list,profile_view,logout_view


urlpatterns = [
    # path('', volunteer_management_view, name='volunteer_management'),
    path('',event_list,name='event_list'),
    path('event/<int:event_id>/',event_details,name='event_detail'),
    path('profile/',profile_view,name='profile_view'),
    path('logout/', logout_view,name='logout')
]
