# Generated by Django 2.1.7 on 2019-04-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0023_remove_ordermodel_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='birth_date',
            field=models.CharField(max_length=30, null=True, verbose_name='Дата рождения'),
        ),
    ]
