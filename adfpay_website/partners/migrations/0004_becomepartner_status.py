# Generated by Django 3.1.3 on 2021-06-21 08:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_auto_20210618_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='becomepartner',
            name='status',
            field=models.CharField(default=datetime.datetime(2021, 6, 21, 8, 47, 26, 716009, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]
