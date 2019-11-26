from rest_framework import serializers
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


class StockSerializer(serializers.ModelSerializer):

    """
    StockSerializer - Will translate objects implemented in Model Stock
    for viewing them in the DRF form.
    """

    class Meta:
        model = Stock
        fields = '__all__'
