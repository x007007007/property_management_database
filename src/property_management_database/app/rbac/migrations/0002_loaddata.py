from django.db import migrations
from ._load_init_data import forwards_func, reverse_func

class Migration(migrations.Migration):
    dependencies = [
        ('pmdb_rbac', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]