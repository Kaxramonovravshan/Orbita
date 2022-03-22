# Generated by Django 3.2.8 on 2022-02-25 12:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20220225_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_favourites', to='app.product', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 12, 43, 25, 868818, tzinfo=utc), verbose_name='Дата создания'),
        ),
    ]
