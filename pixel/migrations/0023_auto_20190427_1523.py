# Generated by Django 2.1.7 on 2019-04-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0022_auto_20190427_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='city_courses',
            field=models.ManyToManyField(default=None, to='pixel.Courses'),
        ),
    ]
