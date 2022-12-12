from django.urls import path
from .views import *    
    
urlpatterns = [   
    path('signup/', SignUpView.as_view(), name='Sign Up'),
    path('login/', AdminLoginView.as_view(), name='Login'),
    path('logout/', AdminLogoutView.as_view(), name='Logout'),
    path('crear_perfil/', crear_perfil, name='Crear Perfil'),
    path('editar_usuario/', editar_usuario, name='Editar Usuario'),
    path('editar_perfil/', editar_perfil, name='Editar Perfil'),
    path('profile/', ver_perfil, name='Ver Perfil'),
    ]