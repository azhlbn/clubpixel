# Generated by Django 2.1.7 on 2019-04-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0030_auto_20190421_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='birth_date',
            field=models.CharField(default='Не указано', max_length=30, verbose_name='Дата рождения'),
        ),
    ]
