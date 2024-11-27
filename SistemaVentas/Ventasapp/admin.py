from django.contrib import admin

# Register your models here.
from .models import Clientes,Empleados,Factura,Productos,Proveedores,Empresas

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'direccion', 'telefono', 'email')
    search_fields = ('cedula', 'nombre', 'apellido')
    list_filter = ('cedula', 'apellido')

@admin.register(Empleados)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'email', 'direccion')
    search_fields = ('cedula', 'apellido')

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad_stock')

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('codigo_factura', 'fecha_factura', 'cliente', 'empleado', 'producto', 'cantidad', 'subtotal', 'iva', 'total')

@admin.register(Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido')

@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('ruc', 'nombre', 'telefono')