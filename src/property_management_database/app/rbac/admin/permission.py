from django.contrib import admin
from ..models import PermissionModel


@admin.register(PermissionModel)
class PermissionModelAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'type',
        'dj_perm',
        'perm_config'
    )