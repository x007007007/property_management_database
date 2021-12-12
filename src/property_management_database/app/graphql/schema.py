import graphene
from property_management_database.app.payment.alipay.graphql import (
    AliyunQuery
)


class Query(AliyunQuery):
    pass


schema = graphene.Schema(query=Query)
