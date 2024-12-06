from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Event


def home(request):
    search_query = request.GET.get('search', '')  # Get the search query from the form
    events = Event.objects.all()  # Fetch all events by default

    if search_query:
        events = events.filter(
            Q(event_type__icontains=search_query) | #search by name
            Q(title__icontains=search_query) |  # Search by title
            Q(location__icontains=search_query)  # Search by location
        )

    return render(request, 'home.html', {'events': events, 'search_query': search_query})


# Event Details View
def event_detail(request, id):
    event = get_object_or_404(Event, id=id)  # Fetch the event by its ID
    return render(request, 'event_detail.html', {'event': event})


# Add New Event
from .forms import EventForm, ContactForm


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)  # Handle uploaded files
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Event updated successfully!')
            return redirect('manage_event')  # Redirect to manage events page
        else:
            print(form.errors)  # Debug: Print form errors
    else:
        form = EventForm()
    return render(request, 'admin/add_event.html', {'form': form})


# Edit Event
def update_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)  # Handle uploaded files and bind to the instance
        if form.is_valid():
            form.save()  # Save the updated event
            messages.success(request, 'Event added successfully!')
            return redirect('manage_event')  # Redirect to the manage events page
        else:
            print(form.errors)  # Debug: Print form errors
    else:
        form = EventForm(instance=event)  # Initialize form with existing data
    return render(request, 'admin/update_event.html', {'form': form, 'event': event})



# Delete Event
def delete_event(request, id):
    event = get_object_or_404(Event, id=id)  # Fetch the event by its ID
    event.delete()  # Delete the event from the database
    messages.success(request, 'Event deleted successfully!')
    return redirect('manage_event')  # Redirect back to the manage events page after deletion


# Static Pages
def events(request):
    return render(request, 'events.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email (optional, you can also save to the database)
            send_mail(
                f'New contact from {name} ({email})',
                message,
                email,
                ['hillarykipngenok7@gmail.com'],  # Replace with your email
                fail_silently=False,
            )

            # Add a success message
            messages.success(request, 'Your message has been sent successfully!')

            # Redirect back to the contact page
            return redirect('contact')  # Redirect to the same page to show the success message

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def manage_events(request):
    events = Event.objects.all()  # Get all events
    return render(request, 'admin/manage_event.html', {'events': events})

