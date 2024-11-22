from django.db import models
from django.template.defaultfilters import length

class raiz(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)

    class Meta:
        abstract = True


class cliente(raiz):
    apellido = models.CharField(max_length=20)
    clave = models.CharField(max_length=50)

class repartidor(raiz):
    moto_marca = models.CharField(max_length=15)
    serie = models.CharField(max_length=15)
    placa = models.CharField(max_length=10)

class restaurante(raiz):
    descripcion = models.TextField(max_length=150)


class plato(models.Model):
    name = models.CharField(max_length=15)
    detail = models.TextField(max_length=200)
    valor = models.CharField(max_length=20)
# Create your models here.

