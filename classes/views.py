from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import MuayClass
from .serializers import MuayClassSerializer
# Create your views here.

class MuayClassViewSet(ModelViewSet):
    queryset = MuayClass.objects.all()
    serializer_class = MuayClassSerializer