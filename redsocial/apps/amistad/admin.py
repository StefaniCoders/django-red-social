from django.contrib import admin

# Register your models here.
from .models.Amistad import Amistad
from .models.SolicitudAmistad import SolicitudAmistad

admin.site.register(Amistad)
admin.site.register(SolicitudAmistad)