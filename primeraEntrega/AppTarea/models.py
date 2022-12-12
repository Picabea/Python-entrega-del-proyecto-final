from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre}, \n Comision: {self.comision}'


class Publicacion(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=50)
    cuerpo = HTMLField()
    autor = models.CharField(max_length=40)
    fecha = models.CharField(max_length=100)
    imagen = models.URLField()
    categoria = models.CharField(max_length=10)

    def __str__(self):
        return f'Titulo: {self.titulo}, subtitulo {self.subtitulo}'

class Comentario(models.Model):
    autor = models.CharField(max_length=40)
    cuerpo = models.CharField(max_length=100)
    publicacion = models.CharField(max_length=10)