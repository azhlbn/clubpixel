# Generated by Django 2.2.1 on 2019-09-03 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0063_auto_20190818_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cities',
            old_name='courses_in_city',
            new_name='courses',
        ),
    ]