from django.db import models
from django.template.defaultfilters import length
from django.contrib.auth.models import User


class Raiz(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nombre}"


class Repartidor(Raiz):
    moto_marca = models.CharField(max_length=15)
    serie = models.CharField(max_length=15)
    placa = models.CharField(max_length=10)
    estado = models.BooleanField(default=True)


class Restaurante(Raiz):
    descripcion = models.TextField(max_length=150)
    logo = models.ImageField(upload_to='logos',null=True)


class Plato(models.Model):
    nombre_plato = models.CharField(max_length=55)
    restaurantes = models.ForeignKey(Restaurante,on_delete=models.CASCADE,default=8)
    detalle = models.TextField(max_length=200)
    valor = models.CharField(max_length=20)
    imagen_plato = models.ImageField(upload_to='platos', null=True)

    def __str__(self):
        return f'{self.nombre_plato}'


class Cliente(Raiz):
    apellido = models.CharField(max_length=20,help_text="Ingrese su apellido")
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
