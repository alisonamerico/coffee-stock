from django.db import models


class Harvest(models.Model):
    cafe_type = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    validity = models.DateField()
    amount_bags = models.IntegerField()


class Stock(models.Model):
    harvest = models.ForeignKey(Harvest, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=150)
    cafes_types = models.CharField(max_length=100)
    quantity_bags_available = models.IntegerField()
    stock_capability = models.IntegerField()


class Farm(models.Model):
    stock = models.ManyToManyField(Stock)
    name = models.CharField(max_length=100)
