# Generated by Django 2.1.2 on 2018-11-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignupModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('tel', models.CharField(max_length=30)),
                ('kid_name', models.CharField(max_length=30)),
                ('kid_age', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Запись на занятия',
                'verbose_name_plural': 'Все записи',
            },
        ),
    ]
