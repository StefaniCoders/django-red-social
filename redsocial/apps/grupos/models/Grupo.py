from django.db import models
from apps.usuarios.models.Usuario import Usuario


class Grupo(models.Model):
    nombre     = models.CharField(max_length=155)
    fecha_crea = models.DateTimeField(editable=False, auto_now_add=True)
    creador    = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nombre', 'fecha_crea', 'creador']
