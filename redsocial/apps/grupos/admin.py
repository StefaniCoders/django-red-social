from django.contrib import admin

# Register your models here.
from .models.Grupo import Grupo
from .models.MenChatSalaGrupo import MenChatSalaGrupo
from .models.Miembro import Miembro
from .models.MiembrosSala import MiembrosSala
from .models.SalaChatGrupo import SalaChatGrupo
from .models.SolicitudGrupo import SolicitudGrupo

admin.site.register(Grupo)
admin.site.register(MenChatSalaGrupo)
admin.site.register(Miembro)
admin.site.register(MiembrosSala)
admin.site.register(SalaChatGrupo)
admin.site.register(SolicitudGrupo)
