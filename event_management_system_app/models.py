from django.db import models
from django.utils import timezone

def upload_event_image(instance, filename):
    return f'events/{instance.title}/{filename}'

from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models

class Event(models.Model):
    # Event Title
    title = models.CharField(max_length=255)

    # Event Description
    description = models.TextField()

    # Event Type (Drop-down options)
    event_type = models.CharField(
        max_length=50,
        choices=[
            ('Technology', 'Technology'),
            ('Education', 'Education'),
            ('Culture', 'Culture'),
            ('Sports', 'Sports'),
            ('Religious', 'Religious'),
            ('Other', 'Other'),
        ]
    )

    # Event Date & Time
    date = models.DateTimeField()

    # Event Location
    location = models.CharField(max_length=255)

    # Ticket Purchase Link (Optional)
    ticket_link = models.URLField(max_length=500, blank=True, null=True)

    # Event Image
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.title



