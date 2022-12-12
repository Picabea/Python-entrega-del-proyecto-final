from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
    user = models.IntegerField()
    avatar = models.URLField()
    descripcion = models.CharField(max_length=150)
    link = models.URLField()


