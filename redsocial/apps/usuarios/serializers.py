from rest_framework import serializers
#from .models import Usuario
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']