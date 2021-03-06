# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-06 22:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20161106_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='empleado', to='payment.EmpresaEmpleadora')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='empleado', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
