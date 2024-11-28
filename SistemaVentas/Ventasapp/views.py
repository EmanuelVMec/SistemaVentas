from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientesSerializer, EmpleadosSerializer, FacturaSerializer, ProductosSerializer, ProveedoresSerializer, EmpresasSerializer
from .models import Clientes, Empleados, Factura, Productos, Proveedores, Empresas

# Create your views here.

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer

class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer

