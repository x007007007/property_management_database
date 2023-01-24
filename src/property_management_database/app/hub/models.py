import os.path

from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.utils import timezone
from django.dispatch.dispatcher import receiver
from mptt.models import MPTTModel, TreeForeignKey


def hub_photo_image_update(object, file):
    ext_name = file.split(".")[-1]
    now = timezone.now()
    fold_path = now.strftime("%Y/%m/%d")
    return f"image/hub_photo/{fold_path}/{object.hub.pk}/{now.timestamp()}.{ext_name}"


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

    def __str__(self):
        return f"<{self.__class__.__name__} ({self.pk} {self.name})>"


@receiver(signal=pre_save, sender=HubOverviewModel)
def on_hub_overview_model_pre_save(sender, instance, **kwargs):
    assert isinstance(instance, HubOverviewModel)
    if instance.pk:
        if old := HubOverviewModel.objects.filter(pk=instance.pk).first():
            if old.image and old.image.path:
                if os.path.exists(old.image.path):
                    old.image.delete(False)


@receiver(signal=pre_delete, sender=HubOverviewModel)
def on_hub_overview_model_pre_delete(sender, instance, **kwargs):
    assert isinstance(instance, HubOverviewModel)
    if instance.image:
        if os.path.exists(instance.image.path):
            instance.image.delete(False)