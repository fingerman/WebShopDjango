# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
