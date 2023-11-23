from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.models import User

class GrupoSerializer(serializers.Serializer):    
    id            = serializers.CharField()
    creador           = serializers.CharField()
    nombre          = serializers.CharField()
    fecha_crea          = serializers.CharField()

class SolicitudGrupoSerializer(serializers.Serializer):    
    id            = serializers.CharField()
    usuario           = serializers.CharField()
    grupo           = serializers.CharField()
    estado          = serializers.CharField()
    fecha       = serializers.CharField()

class SolicitudAmistadSerializer(serializers.Serializer):    
    id            = serializers.CharField()
    usuario1           = serializers.CharField()
    usuario2          = serializers.CharField()
    estado       = serializers.CharField()
    fecha       = serializers.CharField()