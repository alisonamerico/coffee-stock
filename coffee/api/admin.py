from django.contrib import admin
from coffee.api.models import Harvest, Stock, Farm, CafeType


class HarvestAdmin(admin.ModelAdmin):
    list_display = ['cafe_type', 'source', 'validity', 'amount_bags', 'created', 'modified']
    search_fields = ['cafe_type', 'source', 'validity', 'amount_bags']
    list_filter = ['created', 'modified']


class StockAdmin(admin.ModelAdmin):
    list_display = [
        'harvest', 'stock_name', 'quantity_bags_available', 'stock_capability', 'created', 'modified'
    ]
    search_fields = ['harvest', 'stock_name', 'quantity_bags_available', 'stock_capability']
    list_filter = ['created', 'modified']


class CafeTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'created', 'modified']
    search_fields = ['type']
    list_filter = ['created', 'modified']


class FarmAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'modified']
    search_fields = ['name']
    list_filter = ['created', 'modified']


admin.site.register(Harvest, HarvestAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(CafeType, CafeTypeAdmin)
admin.site.register(Farm, FarmAdmin)
