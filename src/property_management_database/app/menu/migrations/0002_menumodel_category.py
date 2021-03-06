# Generated by Django 3.2.10 on 2021-12-15 16:20

from django.db import migrations
import django.db.models.deletion
import property_management_database.app.rbac.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pmdb_rbac', '0006_resourcegroupdimensionmodel_resourcegroupmodel'),
        ('pmdb_menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menumodel',
            name='category',
            field=property_management_database.app.rbac.fields.ResourceGroupForeignKey('menu_category', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
