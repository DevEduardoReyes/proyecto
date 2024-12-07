from django.shortcuts import render, redirect, HttpResponse
from .formulario import Registro
from servicio.models import Cliente,Raiz, Restaurante,Plato,Repartidor
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout , authenticate

def inicio(request):
    return render(request,"inicio.html")


def registrar(request):
    if request.method == 'GET':
        return render(request,'formulario_registro.html',{'formulario':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(username= request.POST['username'], password= request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('inicio')
            except:
                return render(request,'formulario_registro.html',{'formulario':UserCreationForm , 'error':'El usuario ya existe'})
        return render(request,'formulario_registro.html',{'formulario':UserCreationForm , 'error':'Las claves no coinciden'})




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

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request,'inicio_sesion.html', {'sesion': AuthenticationForm})
    else:
        usuario = authenticate(request, username= request.POST['username'], password= request.POST['password'])
        if usuario is None:
            return render(request, 'inicio_sesion.html', {'sesion': AuthenticationForm,                                                        'error':'El usuario que ingreso no existe'})
        else:
            login(request, usuario)
            return redirect('inicio')



