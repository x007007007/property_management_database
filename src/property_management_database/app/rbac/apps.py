from django.apps import AppConfig


class RbacConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'property_management_database.app.rbac'
    label = 'pmdb_rbac'

    def ready(self):
        from .fields import (
            ResourceGroupForeignKeyMeta,
            ResourceGroupForeignKey
        )
        from .models import ResourceGroupDimensionModel
        for gf in ResourceGroupForeignKeyMeta.registor_list():  # type: ResourceGroupForeignKey
            ResourceGroupDimensionModel.objects.get_or_create(name=gf.dimension)