from django.contrib import admin
from .models import (
    RoleModel,
    PermissionModel,
)
# Register your models here.


@admin.register(RoleModel)
class RoleModelAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )


@admin.register(PermissionModel)
class PermissionModelAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'type',
    )