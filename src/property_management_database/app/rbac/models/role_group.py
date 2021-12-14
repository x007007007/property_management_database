from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class RoleGroupModel(MPTTModel):
    name = models.CharField(max_length=254)
    role_set = models.ManyToManyField("RoleModel")
    auth_group = models.ForeignKey(
        "auth.Group",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ['name']