# Generated by Django 2.2.1 on 2019-07-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0048_cities_minecraft'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='kodu',
            field=models.BooleanField(default=False, verbose_name='Kodu'),
        ),
    ]
