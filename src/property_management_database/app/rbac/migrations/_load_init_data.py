from django.core.management import call_command


def forwards_func(apps, schema_editor):
    call_command('loaddata', 'initial/permission_type')


def reverse_func(apps, schema_editor):
    pass

