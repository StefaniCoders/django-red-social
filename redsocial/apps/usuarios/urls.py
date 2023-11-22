from django.urls import path
from .views import ListaUsuarios

urlpatterns = [
    path('usuarios/', ListaUsuarios.as_view(), name='usuarios')
]