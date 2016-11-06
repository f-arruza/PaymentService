from .models import EmpresaEmpleadora
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
