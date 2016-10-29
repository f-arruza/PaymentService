# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
class EmpresaEmpleadora(models.Model):

    TIPO_DOC_PVAL = (
        ('NI', 'NIT'),
        ('CC', 'CEDULA CIUDADANIA'),
        ('CE', 'CEDULA EXTRANJERIA'),
        ('PA', 'PASAPORTE'),
        ('CD', 'CARNE DIPLOMATICO'),
    )

    CLASE_PAGADOR_PVAL = (
        ('A', 'PAGADOR CON MAS DE 200 PENSIONADOS'),
        ('B', 'PAGADOR CON MENOS DE 200 PENSIONADOS'),
        ('I', 'INDEPENDIENTE'),
    )

    NATURALEZA_JURIDICA_PVAL = (
        ('1', 'PUBLICA'),
        ('2', 'PRIVADA'),
        ('3', 'MIXTA'),
    )

    TIPO_PERSONA_PVAL = (
        ('N', 'NATURAL'),
        ('J', 'JURIDICA'),
    )

    TIPO_PAGADOR_PVAL = (
        ('1', 'EMPLEADOR'),
        ('2', 'ADMINISTRADORA PENSIONES'),
        ('3', 'PAGADOR PENSIONES'),
        ('4', 'PENSIONES REGIMEN ESPECIAL'),
    )

    nombreRazonSocial = models.CharField(max_length=150, blank=False)
    tipoDocumento = models.CharField(max_length=2, blank=False,
        choices=TIPO_DOC_PVAL
    )
    numeroDocumento = models.CharField(max_length=16, blank=False)
    clasePagadorPensiones = models.CharField(max_length=1, blank=False,
        choices=CLASE_PAGADOR_PVAL
    )
    naturalezaJuridica = models.CharField(max_length=1, blank=False,
        choices=NATURALEZA_JURIDICA_PVAL
    )
    tipoPersona = models.CharField(max_length=1, blank=False,
        choices=TIPO_PERSONA_PVAL
    )
    direccion = models.CharField(max_length=40, blank=False)
    ciudadMunicipio = models.CharField(max_length=3, blank=False)
    departamento = models.CharField(max_length=2, blank=False)
    telefono = models.CharField(max_length=15, blank=False)
    correo = models.CharField(max_length=60, blank=False)
    tipoPagadorPensiones = models.CharField(max_length=2, blank=False,
        choices=TIPO_PAGADOR_PVAL
    )
    actividadEconomica = models.CharField(max_length=4, blank=False)

    def __str__(self):
        return self.nombreRazonSocial


class Pensionado(models.Model):

    TIPO_DOC_PVAL = (
        ('CC', 'CEDULA CIUDADANIA'),
        ('CE', 'CEDULA EXTRANJERIA'),
        ('TI', 'TARJETA IDENTIDAD'),
        ('RC', 'REGISTRO CIVIL'),
        ('PA', 'PASAPORTE'),
        ('CD', 'CARNE DIPLOMATICO'),
    )

    TIPO_PENSION_PVAL = (
        ('1', 'VEJEZ'),
        ('2', 'SOBREVIVENCIA VITALICIA RIESGO COMUN'),
        ('3', 'SOBREVIVENCIA TEMPORAL RIESGO COMUN'),
        ('4', 'SOBREVIVENCIA TEMPORAL RIESGO COMUN, CONYUGE O COMPAÑERA(O) MENOR DE 30 AÑOS SIN HIJOS'),
        ('5', 'SOBREVIVENCIA VITALICIA RIESGO LABORAL'),
        ('6', 'SOBREVIVENCIA TEMPORAL RIESGO COMUN'),
        ('7', 'SOBREVIVENCIA TEMPORAL RIESGO LABORAL, CONYUGE O COMPAÑERA(O) MENOR DE 30 AÑOS SIN HIJOS'),
        ('8', 'INVALIDEZ RIESGO COMUN'),
        ('9', 'INVALIDEZ RIESGO LABORAL'),
        ('10', 'JUBILACION'),
        ('11', 'JUBILACION PARA COMPARTIR'),
        ('12', 'SANCION'),
        ('13', 'CONVENCIONAL'),
        ('14', 'CONVENCIONAL PARA COMPARTIR'),
        ('15', 'GRACIA'),
        ('16', 'POR CONVENIO INTERNACIONAL'),
        ('20', 'SENTENCIA JUDICIAL'),
        ('21', 'CONCILIACIONES'),
    )

    TIPO_PENSIONADO_PVAL = (
        ('1', 'REGIMEN PRIMA MEDIA, CON TOPE DE PENSION 25 SMMLV'),
        ('2', 'REGIMEN PRIMA MEDIA, SIN TOPE MAXIMO DE PENSION'),
        ('3', 'REGIMEN DE AHORRO INDIVIDUAL'),
        ('4', 'RIESGOS LABORALES, CON TOPE DE PENSION 25 SMMLV'),
        ('5', 'POR EL EMPLEADOR, CON TOPE DE PENSION 25 SMMLV'),
        ('6', 'POR EL EMPLEADOR, SIN TOPE MAXIMA DE PENSION'),
        ('7', 'REGIMENES ESPECIAL O EXCEPCION, CON TOPE DE PENSION 25 SMMLV'),
        ('8', 'REGIMENES ESPECIAL O EXCEPCION, SIN TOPE MAXIMA DE PENSION'),
        ('9', 'BENEFICIO UPC ADICIONAL'),
    )

    TARIFA_ESPECIAL_PVAL = (
        ('1', 'ACTIVIDADES ALTO RIESGO'),
        ('2', 'SENADOR'),
        ('3', 'CTI'),
        ('4', 'AVIADOR'),
    )

    primerApellido = models.CharField(max_length=20, blank=False)
    segundoApellido = models.CharField(max_length=30, blank=True)
    primerNombre = models.CharField(max_length=20, blank=False)
    segundoNombre = models.CharField(max_length=30, blank=True)
    tipoDocumento = models.CharField(max_length=2, blank=False,
        choices=TIPO_DOC_PVAL
    )
    numeroDocumento = models.CharField(max_length=16, blank=False)
    tipoPension = models.CharField(max_length=2, blank=False,
        choices=TIPO_PENSION_PVAL
    )
    tipoPensionado = models.CharField(max_length=1, blank=False,
        choices=TIPO_PENSIONADO_PVAL
    )
    pensionadoExterior = models.BooleanField(default=True, blank=False)
    grupoFamiliarColombia = models.BooleanField(default=True, blank=False)
    ingresoBaseCotizacion = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    actividadEconomica = models.CharField(max_length=4, blank=False)
    tarifaEspecial = models.CharField(max_length=1, blank=False,
        choices=TARIFA_ESPECIAL_PVAL
    )
    empresaEmpleadora = models.ForeignKey(EmpresaEmpleadora, on_delete=models.CASCADE)

    def __str__(self):
        return self.primerApellido + " " + self.primerNombre
