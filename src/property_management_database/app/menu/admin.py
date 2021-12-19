from django.contrib import admin
from guardian.admin import GuardedModelAdminMixin
from mptt.admin import DraggableMPTTAdmin

from property_management_database.app.menu.models import MenuModel


@admin.register(MenuModel)
class MenuModelAdmin(GuardedModelAdminMixin, DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
        'name',
        'category',
    )

