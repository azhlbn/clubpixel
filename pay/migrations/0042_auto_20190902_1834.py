# Generated by Django 2.2.1 on 2019-09-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0041_auto_20190827_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='branches',
            field=models.CharField(max_length=200, null=True, verbose_name='Филиал'),
        ),
    ]
