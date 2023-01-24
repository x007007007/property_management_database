from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ..rbac.fields import ResourceGroupForeignKey


def hub_photo_image_update(object, file):
    return f"image/hub_photo/%Y/%m/%d/{object.pk}"


class HubOverviewModel(models.Model):
    image = models.ImageField(upload_to=hub_photo_image_update)
    hub = models.ForeignKey("HubModel", on_delete=models.CASCADE)


class HubModel(models.Model):
    name = models.CharField(max_length=255, default='')
    code = models.CharField(max_length=16)
    newest_overview = models.ForeignKey(HubOverviewModel, null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey("LocationModel", null=True, blank=True, on_delete=models.SET_NULL)


class LocationModel(MPTTModel):
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children"
    )
    name = models.CharField(max_length=128)
