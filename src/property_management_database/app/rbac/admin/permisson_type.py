from django.contrib import admin
from ..models import PermissionTypeModel


@admin.register(PermissionTypeModel)
class PermissionTypeModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )