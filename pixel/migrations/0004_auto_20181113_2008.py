# Generated by Django 2.1.2 on 2018-11-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0003_auto_20181113_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(default=None, max_length=150, unique=True, verbose_name='URL страницы'),
        ),
    ]
