from django.urls import path
from .views import *

urlpatterns = [
    path('', mostrar_inicio, name='Home'),
    path('pages/<categoria>', ver_publicaciones, name='Publicacion List'),
    path('publicacion_form/', crear_publicacion, name='Publicacion Create'),
    path('publicacion_detalle/<pk>', PublicacionDetail.as_view(), name='Publicacion Detail'),
    path('publicacion_edit/<pk>', PublicacionUpdate.as_view(), name='Publicacion Update'),
    path('publicacion_confirm_delete/<pk>', PublicacionDeleteView.as_view(), name='Publicacion Delete'),
    path('crear_comentario/<id>', crear_comentario, name='Crear Comentario'),
    path('ver_comentarios/<id>', ver_comentarios, name='Comentarios List'),
    path('about', about_us, name='About')
]