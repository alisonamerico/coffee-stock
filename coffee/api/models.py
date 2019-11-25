from django.contrib.postgres.fields import ArrayField
from django.db import models


class Harvest(models.Model):
    cafe_type = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    validity = models.DateField()
    amount_bags = models.IntegerField()

    created = models.DateTimeField('Created in', auto_now_add=True)
    modified = models.DateTimeField('Modified in', auto_now=True)

    class Meta:
        verbose_name = 'Harvest'
        verbose_name_plural = 'Harvest'
        ordering = ['cafe_type']

    def __str__(self):
        return self.cafe_type  # noqa


class Stock(models.Model):
    harvest = models.ForeignKey(Harvest, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=100)
    cafes_types = ArrayField(models.CharField(max_length=150), default=list)
    coffee_farms = ArrayField(models.CharField(max_length=150), default=list)
    quantity_bags_available = models.IntegerField()
    stock_capability = models.IntegerField()

    created = models.DateTimeField('Created in', auto_now_add=True)
    modified = models.DateTimeField('Modified in', auto_now=True)

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'
        ordering = ['stock_name']

    def __str__(self):
        return self.stock_name  # noqa
