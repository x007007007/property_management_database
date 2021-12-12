from django.apps import AppConfig


class GraphqlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'property_management_database.app.graphql'
    label = 'pmdb_app_graphql'
