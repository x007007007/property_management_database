from django.db import models


class PermissionModel(models.Model):
    type = models.ForeignKey(
        'pmdb_rbac.PermissionTypeModel',
        on_delete=models.NOT_PROVIDED,
        null=True,
        blank=True
    )
    dj_perm = models.ForeignKey(
        'auth.Permission',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    perm_config = models.ForeignKey(
        'PermissionConfigModel',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
