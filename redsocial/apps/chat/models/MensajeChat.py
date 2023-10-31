from django.db import models
from .Chat import Chat
from apps.usuarios.models.Usuario import Usuario


class MensajeChat(models.Model):
    usuario      = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha        = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    mensaje_text = models.TextField()

    class Meta:
        ordering = ['usuario', 'fecha', 'mensaje_text']
