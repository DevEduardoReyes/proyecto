from django import forms

from .models import Cliente, Plato


class DatosGenerales(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'direccion', 'telefono']
        help_texts = {
            'nombre': '',
            'apellido': '',
            'direccion': '',
            'telefono': '',
        }





