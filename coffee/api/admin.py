from django.contrib import admin
from coffee.api.models import Harvest, Stock


class HarvestAdmin(admin.ModelAdmin):
    list_display = ['cafe_type', 'source', 'validity', 'amount_bags', 'created', 'modified']
    search_fields = ['cafe_type', 'source', 'validity', 'amount_bags']
    list_filter = ['created', 'modified']


class StockAdmin(admin.ModelAdmin):
    list_display = [
        'harvest', 'stock_name', 'cafes_types', 'coffee_farms', 'quantity_bags_available',
        'stock_capability', 'created', 'modified'
    ]
    search_fields = [
        'harvest', 'stock_name', 'cafes_types', 'coffee_farms', 'quantity_bags_available', 'stock_capability'
    ]
    list_filter = ['created', 'modified']


admin.site.register(Harvest, HarvestAdmin)
admin.site.register(Stock, StockAdmin)
