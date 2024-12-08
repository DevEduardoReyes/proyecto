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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].required = False
        self.fields['apellido'].required = False
        self.fields['direccion'].required = False
        self.fields['telefono'].required = False





