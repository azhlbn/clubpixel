# Generated by Django 2.1.2 on 2018-11-12 13:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20181112_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=ckeditor.fields.RichTextField(default=None, verbose_name='Содержание'),
        ),
    ]
