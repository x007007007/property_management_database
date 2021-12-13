from django.db import models


class UserGroupDimensionModel(models.Model):
    name = models.CharField(max_length=254)