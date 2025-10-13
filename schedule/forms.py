from django import forms
from .models import MuayClass1, Registration, Reviews


class MuayClass1Form(forms.ModelForm):
    class Meta:
        model = MuayClass1
        fields = ['title', 'coach', 'start_time', 'end_time']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'last_name', 'email', 'phone_number']

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'rating', 'review',]