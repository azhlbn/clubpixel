# Generated by Django 2.1.2 on 2018-11-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_auto_20181127_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupmodel',
            name='message',
            field=models.CharField(max_length=70, verbose_name='Дополнительная информация'),
        ),
    ]