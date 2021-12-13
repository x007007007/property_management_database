from django.db import models
from ._base import NameMixin


class PermissionTypeModel(NameMixin, models.Model):
    name = models.CharField(max_length=36)
