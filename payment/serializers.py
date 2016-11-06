from .models import EmpresaEmpleadora, Pensionado
from rest_framework import serializers


class EmpresaEmpleadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaEmpleadora
        fields = (
            'id',
            'nombreRazonSocial',
            'tipoDocumento',
            'numeroDocumento',
            'clasePagadorPensiones',
            'naturalezaJuridica',
            'tipoPersona',
            'direccion',
            'ciudadMunicipio',
            'departamento',
            'telefono',
            'correo',
            'tipoPagadorPensiones',
            'actividadEconomica',
        )


class PensionadoSerializer(serializers.ModelSerializer):
    empresaEmpleadora = EmpresaEmpleadoraSerializer(read_only=True)

    class Meta:
        model = Pensionado
        fields = (
            'id',
            'primerApellido',
            'segundoApellido',
            'primerNombre',
            'segundoNombre',
            'tipoDocumento',
            'numeroDocumento',
            'tipoPension',
            'tipoPensionado',
            'pensionadoExterior',
            'grupoFamiliarColombia',
            'ingresoBaseCotizacion',
            'actividadEconomica',
            'tarifaEspecial',
            'empresaEmpleadora',
        )
