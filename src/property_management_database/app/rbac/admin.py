from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from guardian.admin import GuardedModelAdminMixin
from .models import (
    RoleModel,
    RoleGroupModel,
    UserGroupModel,
    UserGroupBindUserWithRoleModel,
    UserGroupDimensionModel,
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


@admin.register(UserGroupDimensionModel)
class UserGroupDimensionModel(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


@admin.register(RoleGroupModel)
class RoleGroupModelAdmin(GuardedModelAdminMixin, DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
        'name',
    )


@admin.register(UserGroupModel)
class UserGroupModelAdmin(GuardedModelAdminMixin, DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
        'name',
    )
