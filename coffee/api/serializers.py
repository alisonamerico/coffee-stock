from rest_framework import serializers
from rest_framework.fields import ListField

from coffee.api.models import Harvest, Stock


"""
Serializers allow complex data such as querysets and model instances to be converted to native Python
datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide
deserialization, allowing parsed data to be converted back into complex types, after first validating the
incoming data.
"""


class HarvestSerializer(serializers.ModelSerializer):
    """
    HarvestSerializer - Will translate objects implemented in Model Harvest
    for viewing them in the DRF form.
    """
    class Meta:
        model = Harvest
        fields = '__all__'


class StringArrayField(ListField):
    """
    StringArrayField - String representation of an array field.
    """
    def to_representation(self, obj):
        obj = super().to_representation(obj)  # noqa
        # convert list to string
        return ",".join([str(element) for element in obj])  # noqa

    def to_internal_value(self, data):
        data = data.split(",")  # convert string to list  # noqa
        return super().to_internal_value(self, data)  # noqa


class StockSerializer(serializers.ModelSerializer):
    """
    StockSerializer - Will translate objects implemented in Model Stock
    for viewing them in the DRF form.
    """
    cafes_types = StringArrayField()
    coffee_farms = StringArrayField()

    class Meta:
        model = Stock
        fields = '__all__'
