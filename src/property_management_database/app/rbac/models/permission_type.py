from django.db import models
from ._base import NameMixin


class PermissionTypeModel(NameMixin, models.Model):
    TYPE_DJ_MODEL = 'dj_model'
    name = models.CharField(max_length=36)
