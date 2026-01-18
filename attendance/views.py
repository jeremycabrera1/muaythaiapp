from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import (
    extend_schema,
)
from .models import Registration
from .serializers import RegistrationSerializer

@extend_schema(
        request=RegistrationSerializer,
        responses={201: RegistrationSerializer},
        tags = ["Attendance"]
    )
class RegistrationViewSet(ModelViewSet):
    serializer_class = RegistrationSerializer
    queryset = Registration.objects.all()
