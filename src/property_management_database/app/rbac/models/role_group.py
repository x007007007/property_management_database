from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.




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