from django.apps import AppConfig


class RbacConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'property_management_database.app.rbac'
    label = 'pmdb_rbac'
