from django.contrib import admin
from .models import GoodsModel
from .models import GoodsStorageModel


@admin.register(GoodsModel)
class GoodsModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'storage',
    )
    list_filter = (
        'storage',
    )


@admin.register(GoodsStorageModel)
class GoodsStorageModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image'
    )