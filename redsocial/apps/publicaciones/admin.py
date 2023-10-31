from django.contrib import admin

# Register your models here.
from .models.Publicacion import Publicacion
from .models.PublicacionComentario import PublicacionComentario
from .models.PublicacionFile import PublicacionFile
from .models.PublicacionReaccion import PublicacionReaccion

admin.site.register(Publicacion)
admin.site.register(PublicacionComentario)
admin.site.register(PublicacionFile)
admin.site.register(PublicacionReaccion)
