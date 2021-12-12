import graphene_django.filter
from graphene_django import DjangoObjectType
import graphene

from property_management_database.app.payment.alipay.models import (
    BalanceHistoryModel,
    BalanceHistoryCategoryModel,
    BalanceHistoryPaymentTypeModel,
)


class AliyunBalanceHistory(DjangoObjectType):
    class Meta:
        model = BalanceHistoryModel
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith', 'iendswith', 'contains', 'startswith', 'endswith'],
            'datetime': ['exact', 'gt', 'lt', 'range'],
            'payment_type': ['exact'],
            'pmdb_category': ['exact'],
            'number': ['gt', 'lt']
        }
        interfaces = (graphene.Node,)
        fields = (
            'serial_number',
            'name',
            'datetime',
            'remark',
            'number',
            'payment_type',
            'pmdb_category',
        )


class AliyunBalanceHistoryCategory(DjangoObjectType):
    class Meta:
        model = BalanceHistoryCategoryModel
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node,)
        fields = (
            "name",
        )


class AliyunBalanceHistoryPaymentType(DjangoObjectType):
    class Meta:
        model = BalanceHistoryPaymentTypeModel
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node,)
        fields = (
            "name",
        )


class AliyunQuery(graphene.ObjectType):
    aliyun_balance_history = graphene_django.filter.DjangoFilterConnectionField(AliyunBalanceHistory)
    aliyun_balance_payment_type = graphene_django.filter.DjangoFilterConnectionField(AliyunBalanceHistoryPaymentType)
    aliyun_balance_category = graphene_django.filter.DjangoFilterConnectionField(AliyunBalanceHistoryCategory)
