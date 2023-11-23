from django.shortcuts import render
import pymongo
from django.conf import settings

# Create your views here.
from rest_framework import generics
from .models import Usuario
from django.contrib.auth.models import User, Group
from .serializers import GrupoSerializer, SolicitudGrupoSerializer, SolicitudAmistadSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
dbname = client[settings.DB]

def getGrupoAll():

    collection = dbname['grupos_grupo']
    mascot_details = collection.find({})

    return mascot_details

def getSolicitudGrupoAll():
    collection = dbname['grupos_solicitudgrupo']
    mascot_details = collection.find({})

    return mascot_details

def getSolicitudAmistadeAll():
    collection = dbname['amistad_solicitudamistad']
    mascot_details = collection.find({})

    return mascot_details

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