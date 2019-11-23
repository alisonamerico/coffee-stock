from rest_framework import viewsets

from coffee.api.models import Harvest, Stock, Farm


class HarvestViewSet(viewsets.ModelViewSet):
    queryset = Harvest.objects.all()
    # serializer_class = HarvestSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    # serializer_class = StockSerializer


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    # serializer_class = FarmSerializer
