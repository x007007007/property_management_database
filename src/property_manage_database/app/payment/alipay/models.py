from property_manage_database.utils.db import PMDBBaseModel
from django.db import models
# Create your models here.


class BalanceHistoryCategoryModel(PMDBBaseModel):
    name = models.CharField(max_length=64, unique=True)


class BalanceHistoryPaymentTypeModel(PMDBBaseModel):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'<BalanceHistoryPType({self.pk}) {self.name}>'


class BalanceHistoryModel(PMDBBaseModel):
    serial_number = models.CharField(max_length=128)
    name = models.CharField(max_length=255, blank=True, default="")
    datetime = models.DateTimeField(null=True, blank=True)
    remark = models.CharField(max_length=128, default="", blank=True)
    number = models.FloatField()
    payment_type = models.ForeignKey("BalanceHistoryPaymentTypeModel", on_delete=models.NOT_PROVIDED)

    pmdb_category = models.ForeignKey("BalanceHistoryCategoryModel", null=True, blank=True, on_delete=models.SET_NULL)
