from django import forms
from django.forms import ModelForm
from .models import Venue

# Create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = (
            "name",
            "address",
            "zipcode",
            "phone",
            "web",
            "email_address",
        )  # Tuple