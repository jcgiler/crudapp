# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.PositiveIntegerField(verbose_name='Telefono'),
        ),
    ]
