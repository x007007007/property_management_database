from django.contrib import admin

from ..models import PermissionConfigModel


@admin.register(PermissionConfigModel)
class PermissionConfigModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )