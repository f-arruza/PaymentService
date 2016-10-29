# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-29 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pensionado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primerApellido', models.CharField(max_length=20)),
                ('segundoApellido', models.CharField(blank=True, max_length=30)),
                ('primerNombre', models.CharField(max_length=20)),
                ('segundoNombre', models.CharField(blank=True, max_length=30)),
                ('tipoDocumento', models.CharField(choices=[('CC', 'CEDULA CIUDADANIA'), ('CE', 'CEDULA EXTRANJERIA'), ('TI', 'TARJETA IDENTIDAD'), ('RC', 'REGISTRO CIVIL'), ('PA', 'PASAPORTE'), ('CD', 'CARNE DIPLOMATICO')], max_length=2)),
                ('numeroDocumento', models.CharField(max_length=16)),
                ('tipoPension', models.CharField(choices=[('1', 'VEJEZ'), ('2', 'SOBREVIVENCIA VITALICIA RIESGO COMUN'), ('3', 'SOBREVIVENCIA TEMPORAL RIESGO COMUN'), ('4', 'SOBREVIVENCIA TEMPORAL RIESGO COMUN, CONYUGE O COMPAÑERA(O) MENOR DE 30 AÑOS SIN HIJOS'), ('5', 'SOBREVIVENCIA VITALICIA RIESGO LABORAL'), ('6', 'SOBREVIVENCIA TEMPORAL RIESGO COMUN'), ('7', 'SOBREVIVENCIA TEMPORAL RIESGO LABORAL, CONYUGE O COMPAÑERA(O) MENOR DE 30 AÑOS SIN HIJOS'), ('8', 'INVALIDEZ RIESGO COMUN'), ('9', 'INVALIDEZ RIESGO LABORAL'), ('10', 'JUBILACION'), ('11', 'JUBILACION PARA COMPARTIR'), ('12', 'SANCION'), ('13', 'CONVENCIONAL'), ('14', 'CONVENCIONAL PARA COMPARTIR'), ('15', 'GRACIA'), ('16', 'POR CONVENIO INTERNACIONAL'), ('20', 'SENTENCIA JUDICIAL'), ('21', 'CONCILIACIONES')], max_length=2)),
                ('tipoPensionado', models.CharField(choices=[('1', 'REGIMEN PRIMA MEDIA, CON TOPE DE PENSION 25 SMMLV'), ('2', 'REGIMEN PRIMA MEDIA, SIN TOPE MAXIMO DE PENSION'), ('3', 'REGIMEN DE AHORRO INDIVIDUAL'), ('4', 'RIESGOS LABORALES, CON TOPE DE PENSION 25 SMMLV'), ('5', 'POR EL EMPLEADOR, CON TOPE DE PENSION 25 SMMLV'), ('6', 'POR EL EMPLEADOR, SIN TOPE MAXIMA DE PENSION'), ('7', 'REGIMENES ESPECIAL O EXCEPCION, CON TOPE DE PENSION 25 SMMLV'), ('8', 'REGIMENES ESPECIAL O EXCEPCION, SIN TOPE MAXIMA DE PENSION'), ('9', 'BENEFICIO UPC ADICIONAL')], max_length=1)),
                ('pensionadoExterior', models.BooleanField(default=True)),
                ('grupoFamiliarColombia', models.BooleanField(default=True)),
                ('ingresoBaseCotizacion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('actividadEconomica', models.CharField(max_length=4)),
                ('tarifaEspecial', models.CharField(choices=[('1', 'ACTIVIDADES ALTO RIESGO'), ('2', 'SENADOR'), ('3', 'CTI'), ('4', 'AVIADOR')], max_length=1)),
                ('empresaEmpleadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.EmpresaEmpleadora')),
            ],
        ),
    ]
