from django import forms
from tinymce.widgets import TinyMCE

class CrearCurso(forms.Form):
    
    nombre = forms.CharField()
    comision = forms.IntegerField()

class CrearAula(forms.Form):
    materia = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    tamaño = forms.IntegerField()


class CrearEdificio(forms.Form):
    pisos = forms.IntegerField()
    facultad = forms.CharField(max_length=40)
    cantidad_de_aulas = forms.IntegerField()


class CrearComentario(forms.Form):
    cuerpo = forms.CharField(max_length=100)

class CrearPublicacion(forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo =forms.CharField(max_length=50)
    cuerpo = forms.CharField(widget=TinyMCE)
    imagen = forms.URLField()
    categoria = forms.CharField(max_length=10)
