from django.shortcuts import render, redirect, HttpResponse
from .formulario import registro
from .models import cliente,raiz

def inicio(request):
    return render(request,"inicio.html")
# Create your views here.
def log(request):
    if request.method == "GET":
        return render(request,"login.html",
                  {"form":registro()})
    else:
        if request.POST['clave']== request.POST['confirm']:
            cliente.objects.create(
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            direccion=request.POST['direccion'],
            telefono=request.POST['telefono'],
            clave=request.POST['clave'])
            return  HttpResponse("usuario registrado")
        else:
            return render(request, "login.html",
                   {"form": registro()})

