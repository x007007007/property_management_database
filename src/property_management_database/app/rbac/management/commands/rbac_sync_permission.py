from django.core.management.base import BaseCommand, CommandError

from property_management_database.app.rbac.models import (
    PermissionModel,
    PermissionTypeModel,
)
from django.contrib.auth.models import Permission as AuthPerm


class Command(BaseCommand):

    help = 'load django auth permission to rbac permission'

    def handle(self, *args, **options):
        for auth_perm in AuthPerm.objects.all():
            PermissionModel.objects.update_or_create(
                dj_perm=auth_perm,
                type=PermissionTypeModel.objects.get(name=PermissionTypeModel.TYPE_DJ_MODEL)
            )