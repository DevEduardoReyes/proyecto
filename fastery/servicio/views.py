from django.shortcuts import render, redirect, HttpResponse
from .formulario import Registro
from servicio.models import Cliente,Raiz, Restaurante,Plato,Repartidor

def inicio(request):
    return render(request,"inicio.html")

def registrar(request):
    if request.method == "GET":
        return render(request,"formulario_registro.html",
                  {"form":Registro()})
    else:
        if request.POST['clave']== request.POST['confirm']:
            Cliente.objects.create(
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            direccion=request.POST['direccion'],
            telefono=request.POST['telefono'],
            clave=request.POST['clave'])
            return  HttpResponse("usuario registrado")
        else:
            return HttpResponse('Las claves no coinciden')

def res_list(request):
    res = Restaurante.objects.all()
    return render(request,"restaurantes.html",{"res":res})

def menu(request,id):
    comida = Plato.objects.all()
    res = Restaurante.objects.get(nombre=id)
    return render(request, "productos.html",
                  {'comida':comida,
                   "id":id,
                   "res":res})

def no_implementada(request):
    return render(request,"no_implementado.html")

def pedido(request,id):
    orden = Plato.objects.filter(id=id).get()
    return render(request,"confirmar_pedido.html",{"orden":orden})

def realizado(request,id):
    confirma_orden = Plato.objects.filter(id=id).get()
    repartir = Repartidor.objects.filter(id=1).get()
    return render(request,"realizado.html", {"confirma_orden": confirma_orden, "repartir":repartir})