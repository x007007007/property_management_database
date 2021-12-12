import datetime

from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from rangefilter.filters import DateTimeRangeFilter

from property_management_database.app.payment.alipay.models import BalanceHistoryModel


@admin.register(BalanceHistoryModel)
class BalanceHistoryModelAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(BalanceHistoryModelAdmin, self).get_queryset(request)
        return qs.select_related(
            'pmdb_category',
            'payment_type',
        )

    search_fields = (
        'serial_number',
        'name',
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

    list_filter = (
        ('datetime', DateTimeRangeFilter),
        ('pmdb_category', RelatedDropdownFilter),
        ('payment_type', RelatedDropdownFilter),
    )

    def get_rangefilter_datetime_default(self, request):
        # method pattern "get_rangefilter_{field_name}_default"
        return (datetime.datetime.now(), datetime.datetime.now() - datetime.timedelta(days=31))