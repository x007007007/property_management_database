from django.db import models


class PermissionTypeModel(models.Model):
    name = models.CharField(max_length=36)
