# Generated by Django 2.1.7 on 2019-04-27 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0023_auto_20190427_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='city_courses',
        ),
        migrations.AddField(
            model_name='cities',
            name='city_courses',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pixel.Courses'),
        ),
    ]