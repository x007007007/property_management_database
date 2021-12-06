from django.contrib import admin

# Register your models here.

from .models import (
    BalanceHistoryModel,
    BalanceHistoryPaymentTypeModel,
    BalanceHistoryCategoryModel,
    TradingRecordHistoryModel,
)


@admin.register(BalanceHistoryModel)
class BalanceHistoryModelAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'serial_number',
        'name',
        'datetime',
        'remark',
        'payment_type',
        'pmdb_category',
    )
    
    
@admin.register(TradingRecordHistoryModel)
class TradingRecordHistoryModelAdmin(admin.ModelAdmin):
    list_display = (
        "serial_number",
        "order_number",
        "trade_time",
        "payment_time",
        "trade_modify_time",
        "trade_source",
        "trade_transfer_type",
        "trading_party",
        "product",
        "trade_direction",
        "trading_status",
        "funding_status",
        "remark",
        "amount",
        "service_charge",
        "refund",
    )
    