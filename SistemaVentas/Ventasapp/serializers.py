from rest_framework import serializers
from .models import Clientes, Empleados, Factura, Productos, Proveedores, Empresas

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'
    
class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'