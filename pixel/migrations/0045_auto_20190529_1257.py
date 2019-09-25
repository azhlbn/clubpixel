# Generated by Django 2.2.1 on 2019-05-29 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0044_auto_20190529_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='coords',
            field=models.CharField(default=None, help_text='Для определения координат точки, используйте сервис https://yandex.ru/map-constructor/location-tool/. Пример: [55.4325,37.5498]', max_length=30, null=True, verbose_name='Координаты'),
        ),
        migrations.AddField(
            model_name='cities',
            name='zoom',
            field=models.IntegerField(default=None, max_length=10, null=True, verbose_name='Приближение'),
        ),
    ]
