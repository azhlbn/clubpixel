# Generated by Django 2.1.7 on 2019-04-27 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0026_auto_20190427_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='arduino',
        ),
        migrations.RemoveField(
            model_name='cities',
            name='kinder',
        ),
        migrations.RemoveField(
            model_name='cities',
            name='mindstorms',
        ),
        migrations.RemoveField(
            model_name='cities',
            name='mindstormspro',
        ),
        migrations.RemoveField(
            model_name='cities',
            name='scratch',
        ),
        migrations.RemoveField(
            model_name='cities',
            name='wedo',
        ),
    ]
