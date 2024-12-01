from django.db import models
from django.template.defaultfilters import length

class Raiz(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return f"Nombre: {self.nombre}"

class Cliente(Raiz):
    apellido = models.CharField(max_length=20)
    clave = models.CharField(max_length=50)

class Repartidor(Raiz):
    moto_marca = models.CharField(max_length=15)
    serie = models.CharField(max_length=15)
    placa = models.CharField(max_length=10)

class Restaurante(Raiz):
    descripcion = models.TextField(max_length=150)
    logo = models.ImageField(upload_to='logos',null=True)


class Plato(models.Model):
    name = models.CharField(max_length=55)
    nombre_restaurant = models.CharField(max_length=55)
    detail = models.TextField(max_length=200)
    valor = models.CharField(max_length=20)
    imagen_plato = models.ImageField(upload_to='platos', null=True)

    def __str__(self):
        return f'{self.name}'


