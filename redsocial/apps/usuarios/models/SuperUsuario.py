from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.log import log_action


class CustomUserAdmin(UserAdmin):
  list_display = ('username', 'email', 'estado', 'is_active', 'is_staff', 'is_superuser')
  def log_addition(self, request, object):
    log_action(request.user.id, object, 'Add', '')

def log_change(self, request, object, message):
    log_action(request.user.id, object, 'Change', message)

def log_deletion(self, request, object, object_repr):
    log_action(request.user.id, object, 'Delete', object_repr)

admin.site.register(CustomUser, CustomUserAdmin)