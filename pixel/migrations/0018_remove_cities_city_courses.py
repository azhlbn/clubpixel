# Generated by Django 2.1.7 on 2019-04-27 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0017_auto_20190427_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='city_courses',
        ),
    ]
