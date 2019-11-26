from django.contrib.postgres.fields import ArrayField
from django.db import models


"""
A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you’re storing.
Generally, each model maps to a single database table.
"""


class Harvest(models.Model):
    """
    This class contains the representation of the fields in the Harvest table.
    """
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
        """A string representation of the model."""
        return self.cafe_type  # noqa


class Stock(models.Model):
    """
    This class contains the representation of the fields in the Stock table.
    """
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
        """A string representation of the model."""
        return self.stock_name  # noqa
