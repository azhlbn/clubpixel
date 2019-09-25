# Generated by Django 2.1.7 on 2019-04-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0015_slider_details_button1_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='city_courses',
            field=models.CharField(choices=[('kinder', 'Kinder'), ('wedo', 'WeDo'), ('scratch', 'Scratch'), ('ms', 'Mindstorms'), ('mspro', 'Mindstorms Pro'), ('arduino', 'Arduino')], default=None, max_length=200),
        ),
    ]
