from rest_framework import serializers

from .models import MuayClass

class MuayClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuayClass
        fields = ['id', 'title', 'coach', 'start_time', 'end_time']