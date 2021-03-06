# Generated by Django 3.2.10 on 2021-12-12 18:04

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields
import property_management_database.utils.db


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceHistoryCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(property_management_database.utils.db.DisplayNameMixin, models.Model),
        ),
        migrations.CreateModel(
            name='BalanceHistoryPaymentTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(property_management_database.utils.db.DisplayNameMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TradingDirectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=(property_management_database.utils.db.DisplayNameMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TradingFundingStatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=(property_management_database.utils.db.DisplayNameMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TradingPartyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=(property_management_database.utils.db.DisplayNameMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TradingProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=(property_management_database.utils.db.DisplayNameMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TradingRemarkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TradingSourceTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=(property_management_database.utils.db.DisplayNameMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TradingStatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=(property_management_database.utils.db.DisplayNameMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TradingTransferTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=(property_management_database.utils.db.DisplayNameMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TradingRecordHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=128)),
                ('order_number', models.CharField(blank=True, default='', max_length=128)),
                ('trade_time', models.DateTimeField(blank=True, null=True)),
                ('payment_time', models.DateTimeField(blank=True, null=True)),
                ('trade_modify_time', models.DateTimeField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('service_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('refund', models.DecimalField(decimal_places=2, max_digits=20)),
                ('funding_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.fields.NOT_PROVIDED, to='pmdb_payment_alipay.tradingfundingstatusmodel')),
                ('product', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.fields.NOT_PROVIDED, to='pmdb_payment_alipay.tradingproductmodel')),
                ('remark', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.fields.NOT_PROVIDED, to='pmdb_payment_alipay.tradingremarkmodel')),
                ('trade_direction', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.fields.NOT_PROVIDED, to='pmdb_payment_alipay.tradingdirectionmodel')),
                ('trade_source', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.fields.NOT_PROVIDED, to='pmdb_payment_alipay.tradingsourcetypemodel')),
                ('trade_transfer_type', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.fields.NOT_PROVIDED, to='pmdb_payment_alipay.tradingtransfertypemodel')),
                ('trading_party', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.fields.NOT_PROVIDED, to='pmdb_payment_alipay.tradingpartymodel')),
                ('trading_status', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.fields.NOT_PROVIDED, to='pmdb_payment_alipay.tradingstatusmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BalanceHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=128)),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('remark', models.CharField(blank=True, default='', max_length=128)),
                ('number', models.FloatField()),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='pmdb_payment_alipay.balancehistorypaymenttypemodel')),
                ('pmdb_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pmdb_payment_alipay.balancehistorycategorymodel')),
            ],
            options={
                'permissions': (('remark_history', 'You can remark history'),),
            },
        ),
    ]
