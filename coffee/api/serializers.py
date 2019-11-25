from rest_framework import serializers
from rest_framework.fields import ListField

from coffee.api.models import Harvest, Stock


class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = '__all__'


class StringArrayField(ListField):
    """
    String representation of an array field.
    """
    def to_representation(self, obj):
        obj = super().to_representation(self, obj)
        # convert list to string
        return ",".join([str(element) for element in obj])

    def to_internal_value(self, data):
        data = data.split(",")  # convert string to list
        return super().to_internal_value(self, data)


class StockSerializer(serializers.ModelSerializer):
    cafes_types = StringArrayField()
    coffee_farms = StringArrayField()

    class Meta:
        model = Stock
        fields = '__all__'
