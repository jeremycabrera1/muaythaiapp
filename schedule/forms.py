from django import forms
from .models import MuayClass1


class MuayClass1Form(forms.ModelForm):
    class Meta:
        model = MuayClass1
        fields = ['title', 'coach', 'start_time', 'end_time']
