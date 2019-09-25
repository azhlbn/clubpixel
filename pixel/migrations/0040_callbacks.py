# Generated by Django 2.1.3 on 2019-05-15 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0039_auto_20190514_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Callbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50, verbose_name='Имя клиента')),
                ('client_tel', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки на звонок',
            },
        ),
    ]