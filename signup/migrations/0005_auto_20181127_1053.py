# Generated by Django 2.1.2 on 2018-11-27 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20181127_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adr', models.CharField(max_length=100, verbose_name='Адрес филиала')),
            ],
            options={
                'verbose_name': 'Филиал',
                'verbose_name_plural': 'Филиалы',
            },
        ),
        migrations.DeleteModel(
            name='Addresses',
        ),
    ]