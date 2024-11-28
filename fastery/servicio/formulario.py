from django import forms

class registro(forms.Form):
    nombre = forms.CharField(label= "Nombre",max_length=20)
    apellido = forms.CharField(label= "Apellido", max_length=20)
    direccion = forms.CharField(label="Ingrese su direccion",max_length=50)
    telefono = forms.CharField(label="Numero de telefono", max_length=10)
    clave = forms.CharField(widget=forms.PasswordInput)
    confirm = forms.CharField(widget=forms.PasswordInput)



