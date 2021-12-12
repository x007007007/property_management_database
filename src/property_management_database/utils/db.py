from django.db import models
import sys


class PMDBBaseQuerySet(models.QuerySet):
    pass


class PMDBBaseModel(models.Model):
    objects = PMDBBaseQuerySet.as_manager()

    class Meta:
        abstract = True


class DisplayNameMixin:

    def __str__(self):
        if hasattr(str, 'removeprefix'):
            return f"<{self.__class__.__name__.removeprefix('Model')}({self.pk}){self.name}>"
        return f"<{self.__class__.__name__}({self.pk}){self.name}>"


class SoftDeleteMixin(models.Model):
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True
