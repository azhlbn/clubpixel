# Generated by Django 2.1.7 on 2019-04-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0019_cities_city_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название курса')),
            ],
            options={
                'verbose_name': 'Курсы',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
