from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ..rbac.fields import ResourceGroupForeignKey
# Create your models here.


class MenuModel(MPTTModel):
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children"
    )
    name = models.CharField(max_length=128)
    category = ResourceGroupForeignKey("menu_category", on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        permissions = (
            ('view_menu', 'view menu'),
        )
