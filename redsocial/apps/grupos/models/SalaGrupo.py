from django.db import models


class SalaGrupo(models.Model):
    grupo = models.CharField(max_length=155)

    def __str__(self):
        return f'{self.grupo}'