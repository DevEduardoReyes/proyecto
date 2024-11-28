from django.shortcuts import render, redirect, HttpResponse
from .formulario import registro
from servicio.models import cliente,raiz, restaurante,plato

def inicio(request):
    return render(request,"inicio.html")

def log(request):
    if request.method == "GET":
        return render(request,"register.html",
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
            return HttpResponse('Las claves no coinciden')

def res_list(request):
    res = restaurante.objects.all()
    return render(request,"restaurantes.html",{"res":res})

def menu(request,id):
    comida = plato.objects.all()
    res = restaurante.objects.get(nombre=id)
    return render(request, "productos.html",
                  {'comida':comida,
                   "id":id,
                   "res":res})

def no_implementada(request):
    return render(request,"no_implementado.html")

def pedido(request,id):
    orden = plato.objects.filter(id=id).get()
    return render(request,"confirmar_pedido.html",{"orden":orden})

def realizado(request):
    return render(request,"realizado.html")