# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 21:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='address_company',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='name_company',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='country_company',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='email_company',
            new_name='email',
        ),
    ]
