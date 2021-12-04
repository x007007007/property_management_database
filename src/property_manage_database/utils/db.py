from django.db import models


class PMDBBaseQuerySet(models.QuerySet):
    pass


class PMDBBaseModel(models.Model):
    objects = PMDBBaseQuerySet.as_manager()

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True
