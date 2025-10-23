# app_proveedores/models.py

from django.db import models

class Proveedor(models.Model):
    ID_Proveedor = models.AutoField(primary_key=True)
    Nombre_Proveedor = models.CharField(max_length=100)
    Contacto_Nombre = models.CharField(max_length=100)
    Contacto_Telefono = models.CharField(max_length=20, blank=True, null=True) # Opcional
    Contacto_Email = models.EmailField(blank=True, null=True) # Opcional, Django valida email
    Direccion_Proveedor = models.CharField(max_length=255, blank=True, null=True) # Opcional

    def __str__(self):
        return self.Nombre_Proveedor

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['Nombre_Proveedor'] # Ordenar por nombre por defecto