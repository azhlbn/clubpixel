# Generated by Django 2.1.7 on 2019-04-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0021_auto_20190427_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='city_courses',
        ),
        migrations.AddField(
            model_name='cities',
            name='city_courses',
            field=models.ManyToManyField(default=None, null=True, to='pixel.Courses'),
        ),
    ]
