# Generated by Django 2.1.7 on 2019-04-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0029_remove_ordermodel_kids_name2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='birth_date',
            field=models.CharField(max_length=30, verbose_name='Дата рождения'),
        ),
    ]
