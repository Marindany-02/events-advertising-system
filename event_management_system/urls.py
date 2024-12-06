# event_management_system/urls.py
from django.contrib import admin
from django.urls import path, include

from event_management_system_app.views import events

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('event_management_system_app.urls')),  # Replace 'events' with the actual app name
]

