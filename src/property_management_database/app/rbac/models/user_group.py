from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


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