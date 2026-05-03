from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = router.urls