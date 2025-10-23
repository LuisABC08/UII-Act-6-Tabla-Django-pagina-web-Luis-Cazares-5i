# app_proveedores/views.py

from django.shortcuts import render
from .models import Proveedor # Importa tu modelo Proveedor

def index(request):
    # Obtiene todos los objetos Proveedor de la base de datos
    proveedores_lista = Proveedor.objects.all() # Cambié el nombre de la variable para evitar confusión
    context = {
        'proveedores': proveedores_lista # <--- ¡Aquí pasamos la lista con la clave 'proveedores'!
    }
    return render(request, 'app_proveedores/index.html', context)