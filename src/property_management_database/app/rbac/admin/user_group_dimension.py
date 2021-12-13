from django.contrib import admin
from property_management_database.app.rbac.models import UserGroupDimensionModel


@admin.register(UserGroupDimensionModel)
class UserGroupDimensionModel(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )