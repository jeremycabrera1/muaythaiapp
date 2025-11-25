from rest_framework.routers import DefaultRouter
from .views import MuayClassViewSet


router = DefaultRouter()
router.register('classes', MuayClassViewSet, basename='classes')

urlpatterns = router.urls