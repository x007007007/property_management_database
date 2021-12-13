from django.contrib import admin
from guardian.admin import GuardedModelAdminMixin
from mptt.admin import DraggableMPTTAdmin

from property_management_database.app.rbac.models import UserGroupModel


@admin.register(UserGroupModel)
class UserGroupModelAdmin(GuardedModelAdminMixin, DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
        'name',
    )