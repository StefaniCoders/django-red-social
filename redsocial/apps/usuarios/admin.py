from django.contrib import admin

# Register your models here.
from .models.Usuario import Usuario

admin.site.register(Usuario)