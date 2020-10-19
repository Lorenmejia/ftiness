from django.shortcuts import render

from .models import *

def listar_publicaciones(request):
    news = Publicacion.objects.all().order_by('-f_pub')
    return render(request, './post/index.html', {'news':news})

def ver_publicacion(request):
    categoria = categoria.Object.get(id= categoria)
    return render(request,'/post/index.html',{'publicacion':publicacion})

def ver_publicaciones_categoria(request):
    categoria = categoria.Object.get(id= categoria)
    return render(request,'/post/index.html',{'categoria':categoria})
