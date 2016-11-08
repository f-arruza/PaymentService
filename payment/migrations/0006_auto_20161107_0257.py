# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_auto_20161106_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleado', to='payment.EmpresaEmpleadora'),
        ),
    ]