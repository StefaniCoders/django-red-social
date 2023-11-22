from django.shortcuts import render

# Create your views here.
from rest_framework import generics
#from .models import Usuario
from django.contrib.auth.models import User, Group
from .serializers import UsuarioSerializer

class ListaUsuarios(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer