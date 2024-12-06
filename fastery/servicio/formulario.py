from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Widget


class Registro(UserCreationForm):
    nombre = forms.CharField(label= "Nombre",max_length=20)
    apellido = forms.CharField(label= "Apellido", max_length=20)
    direccion = forms.CharField(label="Ingrese su direccion",max_length=50)
    telefono = forms.CharField(label="Numero de telefono", max_length=10)

    class Meta:
        model = User
        fields = ['nombre','apellido','direccion','telefono']
        help_texts={i:'' for i in fields}



