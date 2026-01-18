from drf_spectacular.utils import (
    extend_schema,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import MuayClass
from .serializers import MuayClassSerializer

# Create your views here.

@extend_schema(
        request=MuayClassSerializer,
        responses={201: MuayClassSerializer},
        tags=["Classes"],
    )
class MuayClassModelViewSet(ModelViewSet):
    queryset = MuayClass.objects.all()
    serializer_class = MuayClassSerializer
