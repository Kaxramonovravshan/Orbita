# Generated by Django 3.2.8 on 2022-03-12 09:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_orderfeedback_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderfeedback',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 9, 28, 27, 269315, tzinfo=utc), verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='orderfeedback',
            name='number',
            field=models.CharField(max_length=256, verbose_name='Number'),
        ),
    ]
