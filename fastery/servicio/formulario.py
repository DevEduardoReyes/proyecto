from django import forms

class registro(forms.Form):
    nombre = forms.CharField(label= "Nombre",max_length=20)
    apellido = forms.CharField(label= "Apellido", max_length=20)
    direccion = forms.CharField(label="Ingrese su direccion",max_length=50)
    telefono = forms.CharField(label="Numero de telefono", max_length=10)
    clave = forms.CharField(label="Ingrese su clave", max_length=15)
    confirm = forms.CharField(label="confirme su clave", max_length=15)



