# Generated by Django 3.2.8 on 2022-03-12 08:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20220312_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='number',
            field=models.TextField(max_length=256, verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='orderfeedback',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 8, 56, 7, 591519, tzinfo=utc), verbose_name='Data'),
        ),
    ]
