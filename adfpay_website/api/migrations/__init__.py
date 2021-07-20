from django.db import migrations
from api.models import User


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = User(name="admin@aditsh.com",
                          email="admin@aditsh.com",
                          is_staff=True,
                          is_superuser=True,
                          )
        user.set_password("admin")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]