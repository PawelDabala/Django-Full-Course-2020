# Generated by Django 3.0.2 on 2020-01-22 09:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0002_auto_20200120_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 22, 9, 6, 38, 999776, tzinfo=utc)),
        ),
    ]
