# Generated by Django 3.2.6 on 2022-02-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_date_customuser_gender_customuser_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(max_length=256, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pasport',
            field=models.CharField(max_length=256, null=True, verbose_name='Серия Паспорта'),
        ),
    ]
