from django.contrib import admin

# Register your models here.
from .models.Chat import Chat
from .models.MensajeChat import MensajeChat

admin.site.register(Chat)
admin.site.register(MensajeChat)