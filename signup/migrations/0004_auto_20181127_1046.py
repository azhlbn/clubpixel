# Generated by Django 2.1.2 on 2018-11-27 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20181125_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Адрес филиала')),
            ],
            options={
                'verbose_name': 'Филиал',
                'verbose_name_plural': 'Филиалы',
            },
        ),
        migrations.AlterField(
            model_name='signupmodel',
            name='email',
            field=models.EmailField(max_length=30, unique=True, verbose_name='Email'),
        ),
    ]
