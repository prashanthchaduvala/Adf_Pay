# Generated by Django 3.2 on 2021-07-15 17:47

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210625_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='becomemember',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None, unique=True),
        ),
    ]