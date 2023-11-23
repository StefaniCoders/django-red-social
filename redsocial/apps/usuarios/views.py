from django.shortcuts import render
import pymongo
from django.conf import settings

# Create your views here.
from rest_framework import generics
from .models import Usuario
from django.contrib.auth.models import User, Group
from .serializers import GrupoSerializer, SolicitudGrupoSerializer, SolicitudAmistadSerializer, SalaGrupoSerializer, MiembroGrupoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
dbname = client[settings.DB]

def getGrupoAll():

    collection = dbname['grupos_grupo']
    grupos_grupo = collection.find({})

    return grupos_grupo

def getSolicitudGrupoAll():
    collection = dbname['grupos_solicitudgrupo']
    grupos_solicitudgrupo = collection.find({})

    return grupos_solicitudgrupo

def getSolicitudAmistadeAll():
    collection = dbname['amistad_solicitudamistad']
    amistad_solicitudamistad = collection.find({})

    return amistad_solicitudamistad

def getSalaGrupoAll():
    collection = dbname['grupos_salagrupo']
    amistad_solicitudamistad = collection.find({})

    return amistad_solicitudamistad

def getMiembroGrupoAll():
    collection = dbname['grupos_miembrogrupo']
    amistad_solicitudamistad = collection.find({})

    return amistad_solicitudamistad

@api_view(['GET'])
def obtener_grupos_view(request):
    # Llamas a la función que retorna el array de objetos
    objetos = getGrupoAll()

    # Serializas los objetos usando el serializador
    serialized_objetos = GrupoSerializer(objetos, many=True).data

    # Devuelves la respuesta
    return Response(serialized_objetos)

@api_view(['GET'])
def obtener_solicitud_grupos_view(request):
    # Llamas a la función que retorna el array de objetos
    objetos = getSolicitudGrupoAll()

    # Serializas los objetos usando el serializador
    serialized_objetos = SolicitudGrupoSerializer(objetos, many=True).data

    # Devuelves la respuesta
    return Response(serialized_objetos)

@api_view(['GET'])
def obtener_solicitud_amistatd_view(request):
    # Llamas a la función que retorna el array de objetos
    objetos = getSolicitudAmistadeAll()

    # Serializas los objetos usando el serializador
    serialized_objetos = SolicitudAmistadSerializer(objetos, many=True).data

    # Devuelves la respuesta
    return Response(serialized_objetos)

@api_view(['GET'])
def obtener_sala_grupo_view(request):
    # Llamas a la función que retorna el array de objetos
    objetos = getSalaGrupoAll()

    # Serializas los objetos usando el serializador
    serialized_objetos = SalaGrupoSerializer(objetos, many=True).data

    # Devuelves la respuesta
    return Response(serialized_objetos)

@api_view(['GET'])
def obtener_miembro_grupo_view(request):
    # Llamas a la función que retorna el array de objetos
    objetos = getMiembroGrupoAll()

    # Serializas los objetos usando el serializador
    serialized_objetos = MiembroGrupoSerializer(objetos, many=True).data

    # Devuelves la respuesta
    return Response(serialized_objetos)