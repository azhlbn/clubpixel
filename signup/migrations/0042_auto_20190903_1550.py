# Generated by Django 2.2.1 on 2019-09-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0041_franchise_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='franchise',
            name='tel',
            field=models.CharField(help_text='Правильный формат: +7 (999) 111 22 33', max_length=100, verbose_name='Телефон'),
        ),
    ]