# Generated by Django 3.1.3 on 2021-06-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_auto_20210618_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='becomepartner',
            name='is_partner',
            field=models.BooleanField(default='True'),
        ),
    ]
