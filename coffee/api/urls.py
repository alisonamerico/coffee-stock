from rest_framework import routers

from coffee.api.views import HarvestViewSet, StockViewSet, FarmViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register('harvest', HarvestViewSet)
router.register('stock', StockViewSet)
router.register('farm', FarmViewSet)

urlpatterns = router.urls
