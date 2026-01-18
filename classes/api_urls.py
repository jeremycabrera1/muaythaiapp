from rest_framework.routers import DefaultRouter
from .views import MuayClassModelViewSet


router = DefaultRouter()
router.register('classes', MuayClassModelViewSet, basename='classes')

urlpatterns = router.urls