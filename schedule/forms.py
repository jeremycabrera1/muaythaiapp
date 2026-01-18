from django import forms

from attendance.models import Registration
from classes.models import MuayClass
from reviews.models import Reviews


class MuayClass1Form(forms.ModelForm):
    class Meta:
        model = MuayClass
        fields = ["title", "coach", "start_time", "end_time"]


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ["muay_class"]


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = [
            "owner",
            "rating",
            "review",
        ]
