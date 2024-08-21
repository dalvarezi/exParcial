from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import tema, articulo

# Create your views here.
def directorio(request):
    listaTema = tema.objects.all().order_by('id')
    return render(request,'directorio.html',{
        'listaTema':listaTema
    })

def nuevoTema(request):
    listaTema = tema.objects.all().order_by('id')
    if request.method == 'POST':
        tituloTema = request.POST.get('tituloTema')
        descripcionTema = request.POST.get('descripcionTema')
        objTema = tema.objects.create(
            tituloTema = tituloTema,
            descripcionTema = descripcionTema
            )
        objTema.save()
        return HttpResponseRedirect(reverse('wikiApp:directorio'))
    return render(request,'nuevoTema.html',{
        'listaTema':listaTema
    })

def nuevoArticulo(request): 
    listaTema = tema.objects.all().order_by('id')
    if request.method == 'POST':
        tituloArticulo = request.POST.get('tituloArticulo')
        nombreTema = request.POST.get('nombreTema')
        contenidoArticulo = request.POST.get('contenidoArticulo')
        temaRelacionado = tema.objects.get(id=nombreTema)
        objArticulo = articulo.objects.create(
            tituloArticulo = tituloArticulo,
            contenidoArticulo = contenidoArticulo,
            temaRelacionado = temaRelacionado     
        )
        objArticulo.save()
    return render(request,'nuevoArticulo.html',{
        'listaTema':listaTema
    })

def vistaArticulo(request,idTema):
    listaTema = tema.objects.all().order_by('id')
    objTema = tema.objects.get(id=idTema)
    listaArticulo = objTema.articulo_set.all()
    return render(request,'vistaArticulo.html',{
        'listaTema':listaTema,
        'objTema':objTema,
        'listaArticulo': listaArticulo
    })

def vistaDetalleArticulo(request,idArticulo):
    listaTema = tema.objects.all().order_by('id')
    objArticulo = articulo.objects.get(id=idArticulo)
    return render(request,'vistaDetalleArticulo.html',{
        'listaTema':listaTema,
        'objArticulo':objArticulo, 
    })