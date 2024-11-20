from django.contrib import admin

# Register your models here.
from .models import Clientes, Productos

admin.site.register(Clientes)

admin.site.register(Productos)
