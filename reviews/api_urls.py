from rest_framework.routers import DefaultRouter
from .views import ReviewModelViewSet


router = DefaultRouter()
router.register('reviews', ReviewModelViewSet, basename='reviews')

urlpatterns = router.urls