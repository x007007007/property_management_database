from django.contrib import admin
from ..models import RoleModel


@admin.register(RoleModel)
class RoleModelAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )