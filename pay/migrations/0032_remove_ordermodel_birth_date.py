# Generated by Django 2.1.7 on 2019-04-21 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0031_auto_20190421_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='birth_date',
        ),
    ]
