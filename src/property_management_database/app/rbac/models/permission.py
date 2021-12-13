from django.db import models
from .permission_type import PermissionTypeModel


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

    def __str__(self):

        if self.type.name == PermissionTypeModel.TYPE_DJ_MODEL:
            return f"<{self.__class__.__name__}({self.pk}){self.type.name}:{self.dj_perm.name}>"
        return f"<{self.__class__.__name__}({self.pk}){self.type.name}:{self.perm_config.name}>"