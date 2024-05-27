from django.db import models

# Create your models here.
class Producto(models.Model):
    Codigo = models.CharField(max_length = 100)
    Nombre_Producto = models.CharField(max_length = 150)
    Marca = models.CharField(max_length=150)
    Precio = models.IntegerField()