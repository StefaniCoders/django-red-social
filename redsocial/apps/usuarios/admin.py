from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models.Usuario import Usuario
    
admin.site.register(Usuario)