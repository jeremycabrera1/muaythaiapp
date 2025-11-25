from django.shortcuts import render
from rest_framework.serializers import ModelSerializer
from .models import Registration
from .serializers import RegistrationSerializer
# Create your views here.

class RegistrationViewSet(ModelSerializer):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
