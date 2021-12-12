from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.


class PermissionModel(models.Model):
    type = models.CharField(max_length=32, choices=(
        ('ui', 'ui'),
        ('api', 'api'),
    ))
    rule = models.CharField(max_length=254)


class RoleModel(models.Model):
    name = models.CharField(max_length=254)
    user_set = models.ManyToManyField("auth.User", related_name='role_set')
    group_set = models.ManyToManyField("auth.Group", related_name='role_set')
    permission_set = models.ManyToManyField("PermissionModel", related_name='role_set')


