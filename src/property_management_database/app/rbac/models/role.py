from django.db import models


class RoleModel(models.Model):

    permission_set = models.ManyToManyField(
        "pmdb_rbac.PermissionModel",
        related_name='role_set'
    )
