from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class PermissionTypeModel(models.Model):
    name = models.CharField(max_length=36)


class PermissionModel(models.Model):
    type = models.ForeignKey(
        'PermissionTypeModel',
        on_delete=models.NOT_PROVIDED,
        null=True,
        blank=True
    )
    rule = models.CharField(max_length=254)


class RoleModel(models.Model):
    name = models.CharField(max_length=254)
    auth_group = models.ForeignKey("auth.Group", null=True, blank=True, on_delete=models.SET_NULL)
    permission_set = models.ManyToManyField(
        "PermissionModel",
        related_name='role_set'
    )


class RoleGroupModel(MPTTModel):
    name = models.CharField(max_length=254)
    role_set = models.ManyToManyField("RoleModel")
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ['name']


class UserGroupDimensionModel(models.Model):
    name = models.CharField(max_length=254)


class UserGroupModel(MPTTModel):
    name = models.CharField(max_length=254)
    dimension = models.ForeignKey("UserGroupDimensionModel", on_delete=models.CASCADE)
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )
    user_set = models.ManyToManyField(
        "auth.User",
        through="UserGroupBindUserWithRoleModel",
        related_name="usergroup_set",
        blank=True
    )
    role_group_set = models.ManyToManyField(
        "RoleGroupModel",
        blank=True
    )

    class Meta:
        permissions = (
            ('mgr_sub_group', 'manage sub group'),
        )

    class MPTTMeta:
        order_insertion_by = ['name']


class UserGroupBindUserWithRoleModel(models.Model):
    user_group = models.ForeignKey(
        "UserGroupModel",
        on_delete=models.CASCADE,
        blank=True
    )
    role = models.ForeignKey("RoleModel", on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)