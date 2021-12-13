from django.db import models


class RoleModel(models.Model):
    name = models.CharField(max_length=254)
    auth_group = models.ForeignKey("auth.Group", null=True, blank=True, on_delete=models.SET_NULL)
    permission_set = models.ManyToManyField(
        "pmdb_rbac.PermissionModel",
        related_name='role_set'
    )
