from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from .serializers import ProfileSerializer
from .models import Profile
# Create your views here.

class ProfileModelViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer(queryset, many=True)

class ProfileViewset(ViewSet):

    def list(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)