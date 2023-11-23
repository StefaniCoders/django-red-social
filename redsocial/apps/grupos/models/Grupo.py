from djongo import models
#from django.db import models
from apps.usuarios.models.Usuario import Usuario


class Grupo(models.Model):
    creador    = models.CharField(max_length=155)
    nombre     = models.CharField(max_length=155)
    fecha_crea = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        ordering = ['nombre', 'fecha_crea', 'creador']

    def __str__(self):
        return f'{self.nombre} {self.fecha_crea} {self.creador}'
    