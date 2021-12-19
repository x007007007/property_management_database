from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
from ._base import NameMixin


class ResourceGroupModel(NameMixin, MPTTModel):
    name = models.CharField(max_length=254)
    dimension = models.ForeignKey("ResourceGroupDimensionModel", on_delete=models.CASCADE)
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )

    class Meta:
        permissions = (
            ('mgr_sub_resource_group', 'manage sub resource group'),
        )

    class MPTTMeta:
        order_insertion_by = ['name']
