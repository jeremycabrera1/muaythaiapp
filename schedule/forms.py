from django import forms


from reviews.models import Reviews
from classes.models import MuayClass 
from attendance.models import Registration


class MuayClass1Form(forms.ModelForm):
    class Meta:
        model = MuayClass
        fields = ['title', 'coach', 'start_time', 'end_time']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['muay_class']


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'rating', 'review',]
