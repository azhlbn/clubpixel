# Generated by Django 2.2.1 on 2019-07-15 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0047_auto_20190529_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='minecraft',
            field=models.BooleanField(default=False, verbose_name='Minecraft'),
        ),
    ]
