# Generated by Django 2.1.3 on 2019-05-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0038_auto_20190514_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='leto_wedo',
            field=models.BooleanField(default=False, verbose_name='Летние курсы WeDo'),
        ),
    ]
