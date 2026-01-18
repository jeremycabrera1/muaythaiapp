from drf_spectacular.utils import (
    extend_schema,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Reviews
from .serializers import ReviewSerializer

# Create your views here.


# Right now any user can access any review... I have to make it owner specific
@extend_schema(
    request=ReviewSerializer, responses={201: ReviewSerializer}, tags=["Reviews"]
)
class ReviewModelViewSet(ModelViewSet):
    queryset = Reviews.objects.all().order_by("-date")
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
