from django.contrib import admin
from .models import EmpresaEmpleadora, Empleado, Pensionado


# Register your models here.
@admin.register(EmpresaEmpleadora)
class EmpresaEmpleadoraAdmin(admin.ModelAdmin):
    search_fields = ('nombreRazonSocial', 'tipoDocumento',
                     'numeroDocumento', )


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    search_fields = ('username', 'first_name', 'last_name', )


@admin.register(Pensionado)
class PensionadoAdmin(admin.ModelAdmin):
    search_fields = ('tipoDocumento', 'numeroDocumento', )
