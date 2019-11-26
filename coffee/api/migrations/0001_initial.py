# Generated by Django 2.2.7 on 2019-11-26 14:00

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafe_type', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('validity', models.DateField()),
                ('amount_bags', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created in')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified in')),
            ],
            options={
                'verbose_name': 'Harvest',
                'verbose_name_plural': 'Harvest',
                'ordering': ['cafe_type'],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100)),
                ('cafes_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), default=list, size=None)),
                ('coffee_farms', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), default=list, size=None)),
                ('quantity_bags_available', models.IntegerField()),
                ('stock_capability', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created in')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified in')),
                ('harvest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Harvest')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stock',
                'ordering': ['stock_name'],
            },
        ),
    ]
