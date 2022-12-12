from django.shortcuts import render
from Accounts.models import Perfil
from .models import *
from .forms import CrearComentario, CrearPublicacion
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import time 
# Create your views here.


def mostrar_inicio(request):
    mostrar_info = True
    return render(request, 'index.html', {'info': mostrar_info})
    


@login_required
def crear_comentario(request, id):
    autor = request.user

    if request.method == 'POST':
        formulario = CrearComentario(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            comentario = Comentario(autor=autor, cuerpo=formulario_limpio['cuerpo'], publicacion=id)
            
            comentario.save()
            return render(request, 'index.html', {'info': True})
    else:
        formulario = CrearComentario()
    return render(request, 'crear_comentario.html', {'formulario': formulario})

@login_required
def ver_comentarios(request, id):
    comentarios = Comentario.objects.filter(publicacion=id)
    if len(comentarios) > 0:
        return render(request, "ver_comentarios.html", {'comentarios': comentarios, 'publicacion_id': comentarios[0].publicacion})
    else:
        respuesta = "No hay comentarios"

    return render(request, 'ver_comentarios.html', {'respuesta': respuesta})


def ver_publicaciones(request, categoria):
    if categoria == 'perros' or categoria == 'gatos':
        publicaciones = Publicacion.objects.filter(categoria=categoria)
    else:
        publicaciones = Publicacion.objects.all()
    if len(publicaciones) > 0:
        return render(request, 'publicacion_list.html', {'publicaciones': publicaciones, 'bienvenida': categoria})
    else:
        respuesta = 'No hay publicaciones'
    return render(request, 'publicacion_list.html', {'respuesta': respuesta, 'bienvenida': categoria})

@login_required
def crear_publicacion(request):
    autor = request.user

    if request.method == 'POST':
        formulario = CrearPublicacion(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            tiempo = time.ctime()
            publicacion = Publicacion(
                    titulo = informacion['titulo'],
                    subtitulo = informacion['subtitulo'],
                    cuerpo = informacion['cuerpo'],
                    autor = autor,
                    fecha = tiempo,
                    imagen = informacion['imagen'],
                    categoria = informacion['categoria']

            )
            
            publicacion.save()
            return render(request, 'publicacion_list.html', {'publicaciones': Publicacion.objects.all()})
    else:
        formulario = CrearPublicacion()
    return render(request, 'crear_publicacion.html', {'formulario': formulario})

def about_us(request):
    return render(request, 'about.html')
class PublicacionDetail(LoginRequiredMixin, DetailView):
    model = Publicacion
    template_name = 'AppCoder/publicacion_detalle.html'

class PublicacionUpdate(LoginRequiredMixin, UpdateView):
    model = Publicacion
    template_name = 'AppCoder/publicacion_form.html'
    success_url = '/pages/todos'
    fields = ['titulo', 'subtitulo', 'cuerpo']    

class PublicacionDeleteView(LoginRequiredMixin, DeleteView):
    model = Publicacion
    template_name = 'AppCoder/publicacion_confirm_delete.html'
    success_url = '/pages/todos'

