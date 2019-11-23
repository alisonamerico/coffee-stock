from rest_framework import viewsets

from coffee.api.models import Harvest, Stock
from coffee.api.serializers import HarvestSerializer, StockSerializer


class HarvestViewSet(viewsets.ModelViewSet):
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
