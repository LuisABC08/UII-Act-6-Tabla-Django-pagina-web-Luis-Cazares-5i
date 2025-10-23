# app_proveedores/admin.py

from django.contrib import admin
from .models import Proveedor # Importa tu modelo Proveedor

admin.site.register(Proveedor) # Registra el modelo para que aparezca en el admin
