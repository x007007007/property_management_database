from django.db import models
import datetime


def goods_image_update(object, file):
    return f"image/goods/%Y/%m/%d/{object.pk}"


class GoodsModel(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to=goods_image_update)
    storage = models.ForeignKey("GoodsStorageModel", on_delete=models.CASCADE)


def goods_storage_image_update(object, file):
    return f"image/goods_storage/%Y/%m/%d/{object.pk}"


class GoodsStorageModel(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to=goods_storage_image_update)

