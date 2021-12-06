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
    def get_queryset(self, request):
        qs = super(BalanceHistoryModelAdmin, self).get_queryset(request)
        return qs.select_related(
            'pmdb_category',
            'payment_type',
        )
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
    def get_queryset(self, request):
        qs = super(TradingRecordHistoryModelAdmin, self).get_queryset(request)
        return qs.select_related(
            'trade_source',
            'trade_transfer_type',
            'trading_party',
            'product',
            'trade_direction',
            'trading_status',
            'funding_status',
            'remark',
        )
    search_fields = (
        'serial_number',
        'order_number',
    )
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
    