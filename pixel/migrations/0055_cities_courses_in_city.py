# Generated by Django 2.2.1 on 2019-08-02 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0054_auto_20190802_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='courses_in_city',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pixel.Courses', verbose_name='Укажите курсы в этом городе'),
        ),
    ]
