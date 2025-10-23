# app_proveedores/urls.py

from django.urls import path
from . import views # Importa las vistas de esta aplicación

urlpatterns = [
    path('', views.index, name='index'), # La URL raíz de la aplicación ('/proveedores/' o '/')
]