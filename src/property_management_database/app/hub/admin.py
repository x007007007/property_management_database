from django.contrib import admin
from guardian.admin import GuardedModelAdminMixin
from mptt.admin import DraggableMPTTAdmin

from .models import HubModel
from .models import HubOverviewModel
from .models import LocationModel


@admin.register(HubModel)
class HubModelAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'code',
        'location'
    )


@admin.register(HubOverviewModel)
class HubOverviewModelAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        'image',
    )


@admin.register(LocationModel)
class LocationModelAdmin(GuardedModelAdminMixin, DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
        'name',
    )
    expand_tree_by_default = True