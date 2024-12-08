
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .formulario import DatosGenerales
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


@login_required
def historial(request):
    pedidos = Cliente.objects.filter(usuario=request.user)

    return render(request,'Historial.html',{'pedidos':pedidos})

@login_required
def datos_entrega(request, id):
    plato = Plato.objects.get(id=id)
    repartir = Repartidor.objects.filter(estado=True)
    if not repartir:
        return HttpResponse('No hay repartidores disponibles')
    asignado = repartir.first()
    if request.method == 'POST':
        entrega = DatosGenerales(request.POST)
        if entrega.is_valid():
            asignado.estado = False
            asignado.save()

            historial = entrega.save(commit=False)
            historial.usuario = request.user
            historial.plato = plato
            historial.save()
            return render(request, "realizado.html", {"plato": plato, "repartir": asignado})

    else:
        entrega = DatosGenerales(request.POST)

    return render(request, 'DatosEntrega.html', {'entrega': entrega, 'plato': plato})

def informacion(request):
    return render(request,'acerca_de_nosotros.html')