from django.apps import AppConfig


class AlipayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'property_management_database.app.payment.alipay'
    label = 'pmdb_payment_alipay'
