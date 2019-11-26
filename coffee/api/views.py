from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from coffee.api.models import Harvest, Stock
from coffee.api.serializers import HarvestSerializer, StockSerializer


class HarvestViewSet(viewsets.ModelViewSet):

    """
    HarvestViewSet:
        - Performs queries of objects in the database;
        - Implements search fields and sort filters;
        - Authentication and permission for API access.
    """

    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer
    permission_classes = (IsAuthenticated,)


class StockViewSet(viewsets.ModelViewSet):

    """
    StockViewSet:
        - Performs queries of objects in the database;
        - Implements search fields and sort filters;
        - Authentication and permission for API access.
    """

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAuthenticated,)
