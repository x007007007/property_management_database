from rest_framework import (
    generics,
    serializers
)

from property_manage_database.app.payment.alipay.models import (
    BalanceHistoryModel,
    BalanceHistoryCategoryModel,
    BalanceHistoryPaymentTypeModel,
)
import time


class AliyunBalancePaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceHistoryPaymentTypeModel
        fields = (
            'name',
        )


class AliyunBalanceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceHistoryCategoryModel
        fields = (
            'name',
        )


class AliyunBalanceListSerializer(serializers.ModelSerializer):
    sn = serializers.CharField(source="serial_number", read_only=True)
    payment_type = AliyunBalancePaymentTypeSerializer(read_only=True)
    pmdb_category = AliyunBalanceCategorySerializer(read_only=True)

    class Meta:
        model = BalanceHistoryModel
        read_only_fields = fields = (
            "sn",
            "name",
            "datetime",
            "remark",
            "number",
            "payment_type",
            "pmdb_category",
        )


class AliyunBalanceListApiView(generics.ListAPIView):
    queryset = BalanceHistoryModel.objects.prefetch_related(
        'payment_type',
        'pmdb_category',
    ).order_by('datetime')
    serializer_class = AliyunBalanceListSerializer

    def list(self, request, *args, **kwargs):
        return super(AliyunBalanceListApiView, self).list(request, *args, **kwargs)