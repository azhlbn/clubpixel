# Generated by Django 2.1.3 on 2019-04-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0011_auto_20190424_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='details_button1_url',
            field=models.URLField(default=None, null=True, verbose_name='Ссылка для кнопки'),
        ),
    ]