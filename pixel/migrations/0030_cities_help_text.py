# Generated by Django 2.1.7 on 2019-04-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0029_auto_20190427_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='help_text',
            field=models.CharField(default='Какие курсы доступны в этом городе?', editable=False, max_length=100),
        ),
    ]
