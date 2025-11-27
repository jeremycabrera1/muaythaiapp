from rest_framework.viewsets import ModelViewSet

from .models import Registration
from .serializers import RegistrationSerializer


class RegistrationViewSet(ModelViewSet):
    serializer_class = RegistrationSerializer
    queryset = Registration.objects.all()
