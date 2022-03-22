# Generated by Django 3.2.8 on 2022-02-26 11:56

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0015_alter_product_created_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='add_favourite',
            new_name='Favourite',
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 26, 11, 56, 19, 673789, tzinfo=utc), verbose_name='Дата создания'),
        ),
    ]
