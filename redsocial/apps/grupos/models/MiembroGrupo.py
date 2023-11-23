from django.db import models


class MiembroGrupo(models.Model):
  grupo = models.CharField(max_length=155)
  usuario = models.CharField(max_length=155)
  fecha_entrada = models.DateTimeField(editable=False, auto_now_add=True) 
  rol = models.CharField(max_length=155)
  ultima_conexion = models.DateTimeField(blank=True, null=True, editable=True, auto_now=True)

  def __str__(self):
    return f'{self.grupo}: {self.usuario}'