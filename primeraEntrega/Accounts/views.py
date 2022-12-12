from django.shortcuts import render
from .forms import *
from .models import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = '/'
    template_name = 'AppCoder/registro.html'

class AdminLoginView(LoginView):
    template_name = 'login.html'

class AdminLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'


@login_required
def crear_perfil(request):
    if request.method == 'POST':
       formulario = PerfilForm(request.POST)
       
       if formulario.is_valid():
           formulario_limpio = formulario.cleaned_data
           perfil = Perfil(
               user=request.user.id,
               avatar = formulario_limpio['avatar'],
               descripcion = formulario_limpio['descripcion'],               
               link = formulario_limpio['link']
            )
           perfil.save()
           return render(request, 'index.html', {'info': True})
    else:
       formulario = PerfilForm
    return render(request, 'AppCoder/perfil_form.html', {'form': formulario})

@login_required
def editar_usuario(request):
    usuario = request.user

    if request.method == 'POST':
        usuario_form = UserEditForm(request.POST)

        if usuario_form.is_valid():
            informacion = usuario_form.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()
            return render(request, 'index.html', {'info': True})
        else:
            return render(request, 'AppCoder/admin_update.html', {'form': usuario_form, 'usuario': usuario, 'mensaje': 'Debes modificar todos los campos'})
    else:
        usuario_form = UserEditForm(initial={'username': usuario.username, 'email': usuario.email})

        return render(request, 'AppCoder/admin_update.html', {'form': usuario_form, 'usuario': usuario})

@login_required
def ver_perfil(request):
    user = request.user
    
    usuario = User.objects.filter(username=user.username)
    perfil = Perfil.objects.filter(user=user.id)
    if len(perfil) == 0:
        return render(request, 'sin_perfil.html', {'respuesta': 'Debes crear tu perfil'})
    else:
        return render(request, 'perfil.html', {'perfil': perfil[0], 'usuario': usuario[0], 'url': perfil[0].avatar})
   

@login_required
def editar_perfil(request):
    perfil = Perfil.objects.filter(user=request.user.id)[0]

    if request.method == 'POST':
        perfil_form = PerfilForm(request.POST)

        if perfil_form.is_valid():
            informacion = perfil_form.cleaned_data
            perfil.user = request.user.id
            perfil.avatar = informacion['avatar']
            perfil.descripcion = informacion['descripcion']
            perfil.link = informacion['link']

            perfil.save()

            usuario = User.objects.filter(username=request.user.username)
            perfil = Perfil.objects.filter(user=request.user.id)[0]
            return render(request, 'perfil.html', {'perfil': perfil, 'usuario': usuario[0]})
    else:
        perfil_form = PerfilForm(initial={'avatar': perfil.avatar, 'descripcion': perfil.descripcion, 'link': perfil.link})

        return render(request, 'AppCoder/perfil_form.html', {'form': perfil_form})