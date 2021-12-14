from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
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

    class Meta:
        permissions = (
            ('view_menu', 'view menu'),
        )
