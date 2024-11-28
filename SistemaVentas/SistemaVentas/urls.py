"""
URL configuration for SistemaVentas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Ventasapp.views import ClientesViewSet, EmpleadosViewSet, FacturaViewSet, ProductosViewSet, ProveedoresViewSet, EmpresasViewSet
from rest_framework.routers import DefaultRouter

rutas = DefaultRouter()
rutas.register('Clientes', ClientesViewSet)
rutas.register('Empleados', EmpleadosViewSet)
rutas.register('Factura', FacturaViewSet)
rutas.register('Productos', ProductosViewSet)
rutas.register('Proveedores', ProveedoresViewSet)
rutas.register('Empresas', EmpresasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rutas.urls))
]