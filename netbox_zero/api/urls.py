from rest_framework.routers import DefaultRouter

from .views import DispatcherViewSet
from .views import DeviceJSONViewSet

router = DefaultRouter()
router.register(r'device', DeviceJSONViewSet)
router.register(r'ztp', DispatcherViewSet)
urlpatterns = router.urls

