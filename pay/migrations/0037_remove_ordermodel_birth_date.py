# Generated by Django 2.2.1 on 2019-06-04 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0036_products_crossed_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='birth_date',
        ),
    ]
