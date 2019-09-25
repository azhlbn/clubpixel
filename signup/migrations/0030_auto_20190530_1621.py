# Generated by Django 2.2.1 on 2019-05-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0029_branches_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branches',
            name='body',
        ),
        migrations.AddField(
            model_name='branches',
            name='description_url',
            field=models.URLField(default=None, null=True, verbose_name='Ссылка внутри метки'),
        ),
    ]