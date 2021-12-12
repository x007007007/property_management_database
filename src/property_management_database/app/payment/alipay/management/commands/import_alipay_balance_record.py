from dateutil.parser import parse as datetime_parse
from dateutil.tz import gettz
from django.core.management.base import BaseCommand, CommandError
from property_management_database.app.payment.alipay.models import (
    BalanceHistoryModel,
    BalanceHistoryPaymentTypeModel,
)
import csv


class Command(BaseCommand):

    help = 'load alipay exported balance csv file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        with open(options['path'], encoding='gbk') as fp:
            while res := fp.readline():
                if "收支明细列表" in res:
                    break
            res = csv.DictReader(fp, delimiter=',')
            for row in res:
                match row['资金渠道']:
                    case str(x):
                        t, _ = BalanceHistoryPaymentTypeModel.objects.get_or_create(
                            name=x.strip()
                        )
                    case None:
                        t = None
                sn = row['流水号'].strip()
                if not sn.startswith("#"):
                    BalanceHistoryModel.objects.update_or_create(
                        defaults=dict(
                            datetime=datetime_parse(row['时间']).replace(tzinfo=gettz('Asia/Shanghai')),
                            name=row['名称'],
                            remark=row['备注'],
                            number=float(row['收入'] or row['支出']),
                            payment_type=t
                        ),
                        serial_number=sn
                    )


