# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0011_auto_20181025_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
        ),
    ]
