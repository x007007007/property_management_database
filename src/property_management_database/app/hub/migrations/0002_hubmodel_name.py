# Generated by Django 3.2.10 on 2023-01-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmdb_app_hub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hubmodel',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
