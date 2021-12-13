from django.db import models
from ._base import NameMixin


class PermissionConfigModel(NameMixin, models.Model):
    name = models.CharField(max_length=254)
    rule = models.TextField()
