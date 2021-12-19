from django.contrib import admin

from ..models import ResourceGroupDimensionModel


@admin.register(ResourceGroupDimensionModel)
class ResourceGroupDimensionModelAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )