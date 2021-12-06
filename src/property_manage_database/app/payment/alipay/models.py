from property_manage_database.utils.db import PMDBBaseModel, DisplayNameMixin
from django.db import models


# Create your models here.


class BalanceHistoryCategoryModel(DisplayNameMixin, PMDBBaseModel):
    name = models.CharField(max_length=64, unique=True)


class BalanceHistoryPaymentTypeModel(DisplayNameMixin, PMDBBaseModel):
    name = models.CharField(max_length=64, unique=True)


class BalanceHistoryModel(PMDBBaseModel):
    serial_number = models.CharField(max_length=128)
    name = models.CharField(max_length=255, blank=True, default="")
    datetime = models.DateTimeField(null=True, blank=True)
    remark = models.CharField(max_length=128, default="", blank=True)
    number = models.FloatField()
    payment_type = models.ForeignKey("BalanceHistoryPaymentTypeModel", on_delete=models.NOT_PROVIDED)

    pmdb_category = models.ForeignKey("BalanceHistoryCategoryModel", null=True, blank=True, on_delete=models.SET_NULL)


class TradingSourceTypeModel(DisplayNameMixin, PMDBBaseModel):
    name = models.CharField(max_length=128)


class TradingTransferTypeModel(DisplayNameMixin, PMDBBaseModel):
    name = models.CharField(max_length=128)


class TradingPartyModel(DisplayNameMixin, PMDBBaseModel):
    name = models.CharField(max_length=128)


class TradingProductModel(DisplayNameMixin, PMDBBaseModel):
    name = models.CharField(max_length=128)


class TradingStatusModel(DisplayNameMixin, PMDBBaseModel):
    name = models.CharField(max_length=128)


class TradingDirectionModel(DisplayNameMixin, PMDBBaseModel):
    name = models.CharField(max_length=128)


class TradingRemarkModel(PMDBBaseModel):
    remark = models.TextField()


class TradingFundingStatusModel(DisplayNameMixin, PMDBBaseModel):
    name = models.CharField(max_length=128)


class TradingRecordHistoryModel(PMDBBaseModel):
    serial_number = models.CharField(max_length=128)
    order_number = models.CharField(max_length=128, blank=True, default="")
    trade_time = models.DateTimeField(null=True, blank=True)
    payment_time = models.DateTimeField(null=True, blank=True)
    trade_modify_time = models.DateTimeField(null=True, blank=True)
    trade_source = models.ForeignKey(
        "TradingSourceTypeModel",
        null=True,
        blank=True,
        editable=False,
        on_delete=models.NOT_PROVIDED,
    )
    trade_transfer_type = models.ForeignKey(
        "TradingTransferTypeModel",
        null=True,
        blank=True,
        editable=False,
        on_delete=models.NOT_PROVIDED,
    )
    trading_party = models.ForeignKey(
        "TradingPartyModel",
        null=True,
        blank=True,
        editable=False,
        on_delete=models.NOT_PROVIDED,
    )
    product = models.ForeignKey(
        "TradingProductModel",
        null=True,
        blank=True,
        editable=False,
        on_delete=models.NOT_PROVIDED,
    )
    trade_direction = models.ForeignKey(
        "TradingDirectionModel",
        null=True,
        blank=True,
        editable=False,
        on_delete=models.NOT_PROVIDED,
    )
    trading_status = models.ForeignKey(
        "TradingStatusModel",
        null=True,
        blank=True,
        editable=False,
        on_delete=models.NOT_PROVIDED,
    )
    funding_status = models.ForeignKey(
        "TradingFundingStatusModel",
        null=True,
        blank=True,
        on_delete=models.NOT_PROVIDED,
    )
    remark = models.ForeignKey(
        "TradingRemarkModel",
        null=True,
        blank=True,
        on_delete=models.NOT_PROVIDED,
    )

    amount = models.DecimalField(decimal_places=2, max_digits=20)
    service_charge = models.DecimalField(decimal_places=2, max_digits=10)
    refund = models.DecimalField(decimal_places=2, max_digits=20)
