# Generated by Django 2.1.3 on 2019-04-24 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0009_merge_20190422_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название города')),
                ('flag', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
    ]
