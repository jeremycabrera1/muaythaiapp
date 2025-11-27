from rest_framework import serializers

from .models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.id")

    class Meta:
        model = Registration
        fields = ["id", "owner", "muay_class"]
