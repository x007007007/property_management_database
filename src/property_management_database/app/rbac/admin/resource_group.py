from django.contrib import admin
from guardian.admin import GuardedModelAdminMixin
from mptt.admin import DraggableMPTTAdmin

from ..models import ResourceGroupModel


@admin.register(ResourceGroupModel)
class RoleGroupModelAdmin(GuardedModelAdminMixin, DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
        'name',
        'dimension',
    )

    list_filter = (
        'dimension',
    )

    search_fields = (
        'name',
    )