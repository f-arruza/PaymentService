# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_auto_20161107_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Novedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('fechaCreacion', models.DateField(auto_now_add=True)),
                ('tipo', models.CharField(choices=[('01', 'TRASLADO'), ('02', 'VARIACION TRANSITORIA DEL SALARIO'), ('03', 'SLN - SUSPENSION TEMPORAL, LICENCIA NO REMMUNERADA O COMISION DE SERVICIOS'), ('04', 'INCAPACIDAD TEMPORAL POR ENFERMEDAD'), ('05', 'LICENCIA DE MATERNIDAD O PATERNIDAD'), ('06', 'VACACIONES'), ('07', 'LICENCIA REMUNEDARA'), ('08', 'APORTE VOLUNTARIO A PENSIONES'), ('09', 'SUSPENSION')], max_length=2)),
                ('procesada', models.BooleanField(default=False)),
                ('duracion', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('pensionado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.Pensionado')),
            ],
        ),
    ]
