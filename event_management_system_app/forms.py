from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_type', 'date', 'location','image', 'ticket_link']

    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 50, 'placeholder': 'Short event description...'}),
        required=False  # Optional: description can be empty
    )

    # Optionally, you can add other custom widgets for better user experience.
    ticket_link = forms.URLField(
        widget=forms.URLInput(attrs={'placeholder': 'External ticket link (if any)'}),
        required=False
    )
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

