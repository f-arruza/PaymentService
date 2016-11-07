# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_banco_pagoaporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagoaporte',
            name='tipo',
            field=models.CharField(choices=[('01', 'SALUD'), ('02', 'PENSION'), ('03', 'RIESGOS LABORALES')], max_length=2),
        ),
    ]
