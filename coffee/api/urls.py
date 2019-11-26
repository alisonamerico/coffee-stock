from rest_framework import routers

from coffee.api.views import HarvestViewSet, StockViewSet

"""
Registration of urls available in the application
"""

router = routers.DefaultRouter(trailing_slash=True)

router.register('harvest', HarvestViewSet)
router.register('stock', StockViewSet)


urlpatterns = router.urls
