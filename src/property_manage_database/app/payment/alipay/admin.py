from django.contrib import admin

# Register your models here.

from .models import BalanceHistoryModel


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