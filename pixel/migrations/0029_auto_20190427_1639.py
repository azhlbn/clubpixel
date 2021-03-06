# Generated by Django 2.1.7 on 2019-04-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0028_auto_20190427_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='arduino',
            field=models.BooleanField(default=True, verbose_name='Arduino'),
        ),
        migrations.AlterField(
            model_name='cities',
            name='kinder',
            field=models.BooleanField(default=True, verbose_name='Kinder'),
        ),
        migrations.AlterField(
            model_name='cities',
            name='mindstorms',
            field=models.BooleanField(default=True, verbose_name='Mindstorms'),
        ),
        migrations.AlterField(
            model_name='cities',
            name='mindstormspro',
            field=models.BooleanField(default=True, verbose_name='Mindstorms Pro'),
        ),
        migrations.AlterField(
            model_name='cities',
            name='scratch',
            field=models.BooleanField(default=True, verbose_name='Scratch'),
        ),
        migrations.AlterField(
            model_name='cities',
            name='wedo',
            field=models.BooleanField(default=True, verbose_name='WeDo'),
        ),
    ]
