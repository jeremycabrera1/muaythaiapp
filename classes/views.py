from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from .models import MuayClass
from .serializers import MuayClassSerializer
# Create your views here.

# class MuayClassModelViewSet(ModelViewSet):
#     queryset = MuayClass.objects.all()
#     serializer_class = MuayClassSerializer

class MuayClassViewSet(ViewSet):
    def list(self, request):
        queryset = MuayClass.objects.all()
        serializer = MuayClassSerializer(queryset, many=True)
        return Response(serializer.data)