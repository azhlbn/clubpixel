# Generated by Django 2.1.3 on 2019-05-02 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0023_auto_20190502_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branches',
            name='branch_city',
        ),
    ]
