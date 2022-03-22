# Generated by Django 3.2.8 on 2022-02-26 12:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20220226_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='product',
        ),
        migrations.AddField(
            model_name='favourite',
            name='ProductColorSize',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_favourites', to='app.productcolorsize', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 26, 12, 3, 38, 147267, tzinfo=utc), verbose_name='Дата создания'),
        ),
    ]
