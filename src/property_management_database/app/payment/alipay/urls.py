from django.urls import (
    path,
    include,
)
from . import rest
from asgiref.sync import sync_to_async


urlpatterns = [
    path('balance/list/', sync_to_async(rest.balance.list.AliyunBalanceListApiView.as_view())),
]