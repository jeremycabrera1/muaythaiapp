from rest_framework.routers import DefaultRouter
from .views import ProfileModelViewSet, ProfileViewset

router = DefaultRouter()
router.register('profiles', ProfileViewset, basename='profiles')

urlpatterns = router.urls