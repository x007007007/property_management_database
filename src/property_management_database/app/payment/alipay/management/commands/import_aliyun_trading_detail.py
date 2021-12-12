import collections
import contextlib
import decimal
import functools
import zipfile
import io
from dateutil.parser import parse as datetime_parse
from dateutil.tz import gettz
from django.core.management.base import BaseCommand, CommandError
from property_management_database.app.payment.alipay.models import (
    TradingRemarkModel,
    TradingPartyModel,
    TradingProductModel,
    TradingStatusModel,
    TradingDirectionModel,
    TradingSourceTypeModel,
    TradingTransferTypeModel,
    TradingFundingStatusModel,
    TradingRecordHistoryModel,
)
import csv


class Command(BaseCommand):

    help = 'load alipay record detail from zip or csv'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    trans_datetime_fn = lambda x: datetime_parse(x).replace(tzinfo=gettz("Asia/Shanghai")) if x else None
    trans_fk = lambda field_name, model, value: (model.objects.get_or_create(**{field_name: value})[0]) if value else None

    trans_map = {
        "交易号": ('serial_number', str),
        "商家订单号": ('order_number', str),
        "交易创建时间": ("trade_time", trans_datetime_fn),
        "付款时间": ('payment_time', trans_datetime_fn),
        "最近修改时间": ("trade_modify_time", trans_datetime_fn),
        "交易来源地": ("trade_source", functools.partial(trans_fk, 'name', TradingSourceTypeModel)),
        "类型": ("trade_transfer_type", functools.partial(trans_fk, 'name', TradingTransferTypeModel)),
        "交易对方": ("trading_party", functools.partial(trans_fk, 'name', TradingPartyModel)),
        "商品名称": ("product", functools.partial(trans_fk, 'name', TradingProductModel)),
        "金额（元）": ("amount", decimal.Decimal),
        "收/支": ("trade_direction", functools.partial(trans_fk, 'name', TradingDirectionModel)),
        "交易状态": ("trading_status", functools.partial(trans_fk, 'name', TradingStatusModel)),
        "服务费（元）": ("service_charge", float),
        "成功退款（元）": ("refund", decimal.Decimal),
        "备注": ("remark", functools.partial(trans_fk, 'remark', TradingRemarkModel)),
        "资金状态": ("funding_status", functools.partial(trans_fk, 'name', TradingFundingStatusModel)),
    }

    @contextlib.contextmanager
    def read_file(self, file_path):
        fp = None
        if file_path.endswith(".zip"):
            zfp = zipfile.ZipFile(file_path, "r")
            assert len(zfp.filelist) == 1
            for fp in zfp.filelist:
                fp = io.TextIOWrapper(zfp.open(fp.filename, 'r'), encoding='GBK')
        else:
            fp = open(file_path, 'r', encoding='GBK')
        try:
            yield fp
        finally:
            if fp:
                fp.close()

    def handle(self, *args, **options):
        with self.read_file(options['path']) as fp:
            is_correct_record_type = False
            while res := fp.readline():
                if not is_correct_record_type and '支付宝交易记录明细查询' in res:
                    is_correct_record_type = True
                if "交易记录明细列表" in res:
                    break
            if not is_correct_record_type:
                CommandError("file type error")
                return
            fieldnames = [i.strip() for i in fp.readline().split(",")]
            field_len = len(fieldnames)
            while row := fp.readline():
                row_items = [i.strip() for i in row.split(",")]
                if len(row_items) != field_len:
                    break
                m = collections.OrderedDict(zip(fieldnames, row_items))
                update_fields = {}
                for care_item, (update_field_name, trans_fun) in self.trans_map.items():
                    update_fields[update_field_name] = trans_fun(m[care_item])
                update_key = update_fields.pop('serial_number')
                TradingRecordHistoryModel.objects.update_or_create(
                    defaults=update_fields,
                    serial_number=update_key
                )
