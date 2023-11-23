from django.db import models
from apps.usuarios.models.Usuario import Usuario

ESTADOS = [
    (0, 'Pendiente'),
    (1, 'Rechazado'),
    (2, 'Aceptado')
]

class SolicitudAmistad(models.Model):
    usuario1 = models.CharField(max_length=155)
    usuario2 = models.CharField(max_length=155)
    estado   = models.IntegerField(choices=ESTADOS, default=0)
    fecha    = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    class Meta:
        ordering = ['usuario1', 'usuario2', 'estado', 'fecha']