# Generated by Django 2.1.7 on 2019-04-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0035_remove_products_crossed_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='crossed_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True, verbose_name='Зачеркнутая цена абонемента'),
        ),
    ]
