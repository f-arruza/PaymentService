from django.contrib import admin
from .models import EmpresaEmpleadora, Pensionado

# Register your models here.
@admin.register(EmpresaEmpleadora)
class EmpresaEmpleadoraAdmin(admin.ModelAdmin):
    search_fields = ('nombreRazonSocial', 'tipoDocumento',
        'numeroDocumento', )

@admin.register(Pensionado)
class PensionadoAdmin(admin.ModelAdmin):
    search_fields = ('tipoDocumento', 'numeroDocumento', )
