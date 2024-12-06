from django.contrib import admin
from .models import Category, Event



admin.site.register(Event)
# admin.py
from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'event_type', 'date', 'location', 'price', 'ticket_link']
    search_fields = ['name', 'event_type']

