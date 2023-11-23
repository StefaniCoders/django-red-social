#from djongo import models
from django.db import models
import pymongo

# defailt blank=False, null=False -> no puede ser vacio, obligatorio

GENEROS = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro')
]

class Usuario(models.Model):
    email           = models.EmailField(max_length=155)
    nombre          = models.CharField(max_length=155)
    apellidos       = models.CharField(max_length=155)
    fecha_reg       = models.DateTimeField(editable=False, auto_now_add=True) 
    genero          = models.CharField(max_length=1, choices=GENEROS)
    passw           = models.CharField(max_length=155)
    imagen_perfil   = models.ImageField(upload_to='apps/usuarios/imagenesPerfil/', blank=True, null=True)
    fecha_nac       = models.DateField(blank=True, null=True, editable=True)
    ultima_conexion = models.DateTimeField(blank=True, null=True, editable=True, auto_now=True)