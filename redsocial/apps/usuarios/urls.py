from django.urls import path
from .views import obtener_grupos_view, obtener_solicitud_grupos_view, obtener_solicitud_amistatd_view,obtener_miembro_grupo_view,obtener_sala_grupo_view

urlpatterns = [
    path('grupos/', obtener_grupos_view, name='grupos'),
    path('solicitud-grupo/', obtener_solicitud_grupos_view, name='solicitud-grupo'),
    path('solicitud-amistad/', obtener_solicitud_amistatd_view, name='solicitud-amistad'),
    path('miembro-grupo/', obtener_miembro_grupo_view, name='miembro-grupo'),
    path('sala-grupo/', obtener_sala_grupo_view, name='sala-grupo')
]