# Generated by Django 2.2.1 on 2019-08-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0031_auto_20190530_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signupmodel',
            name='message',
        ),
        migrations.RemoveField(
            model_name='signupmodel',
            name='surname',
        ),
        migrations.AddField(
            model_name='signupmodel',
            name='service',
            field=models.CharField(default='Запись на пробное занятие', max_length=70, verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='signupmodel',
            name='kid_age',
            field=models.CharField(max_length=30, verbose_name='Дата рождения ученика'),
        ),
        migrations.AlterField(
            model_name='signupmodel',
            name='kid_name',
            field=models.CharField(max_length=30, verbose_name='ФИО ученика'),
        ),
        migrations.AlterField(
            model_name='signupmodel',
            name='name',
            field=models.CharField(max_length=30, verbose_name='ФИО контактного лица'),
        ),
    ]