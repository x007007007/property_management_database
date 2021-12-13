from django.db import models


class PermissionModel(models.Model):
    type = models.ForeignKey(
        'pmdb_rbac.PermissionTypeModel',
        on_delete=models.NOT_PROVIDED,
        null=True,
        blank=True
    )
    rule = models.CharField(max_length=254)