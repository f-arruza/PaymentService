# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-29 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaEmpleadora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreRazonSocial', models.CharField(max_length=150)),
                ('tipoDocumento', models.CharField(choices=[('NI', 'NIT'), ('CC', 'CEDULA CIUDADANIA'), ('CE', 'CEDULA EXTRANJERIA'), ('PA', 'PASAPORTE'), ('CD', 'CARNE DIPLOMATICO')], max_length=2)),
                ('numeroDocumento', models.CharField(max_length=16)),
                ('clasePagadorPensiones', models.CharField(choices=[('A', 'PAGADOR CON MAS DE 200 PENSIONADOS'), ('B', 'PAGADOR CON MENOS DE 200 PENSIONADOS'), ('I', 'INDEPENDIENTE')], max_length=1)),
                ('naturalezaJuridica', models.CharField(choices=[('1', 'PUBLICA'), ('2', 'PRIVADA'), ('3', 'MIXTA')], max_length=1)),
                ('tipoPersona', models.CharField(choices=[('N', 'NATURAL'), ('J', 'JURIDICA')], max_length=1)),
                ('direccion', models.CharField(max_length=40)),
                ('ciudadMunicipio', models.CharField(max_length=3)),
                ('departamento', models.CharField(max_length=2)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=60)),
                ('tipoPagadorPensiones', models.CharField(choices=[('1', 'EMPLEADOR'), ('2', 'ADMINISTRADORA PENSIONES'), ('3', 'PAGADOR PENSIONES'), ('4', 'PENSIONES REGIMEN ESPECIAL')], max_length=2)),
                ('actividadEconomica', models.CharField(max_length=4)),
            ],
        ),
    ]
