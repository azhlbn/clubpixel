# Generated by Django 2.1.3 on 2019-05-14 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0037_auto_20190514_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='leto_wedo',
            field=models.BooleanField(default=True, verbose_name='Летние курсы WeDo'),
        ),
    ]
