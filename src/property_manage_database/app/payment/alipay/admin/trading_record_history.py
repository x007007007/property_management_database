from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from rangefilter.filters import DateTimeRangeFilter

from property_manage_database.app.payment.alipay.models import TradingRecordHistoryModel


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

    list_filter = (
        ('payment_time', DateTimeRangeFilter),
        ('trade_transfer_type', RelatedDropdownFilter),
        ('trade_source', RelatedDropdownFilter),
        ('product', RelatedDropdownFilter),
        ('trade_direction', RelatedDropdownFilter),
        ('trading_status', RelatedDropdownFilter),
        ('funding_status', RelatedDropdownFilter),
        ('trading_party', RelatedDropdownFilter),
    )