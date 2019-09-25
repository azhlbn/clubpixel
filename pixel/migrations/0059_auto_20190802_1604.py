# Generated by Django 2.2.1 on 2019-08-02 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0058_auto_20190802_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='bg_image',
            field=models.ImageField(default='default_courses_bg.jpg', help_text='385 px на 531 px', upload_to='courses_image', verbose_name='Фоновое изображение'),
        ),
        migrations.AddField(
            model_name='courses',
            name='btn_color',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pixel.Courses', verbose_name='Выберите цвет кнопки'),
        ),
        migrations.AddField(
            model_name='courses',
            name='string_1',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='1-я строка'),
        ),
        migrations.AddField(
            model_name='courses',
            name='string_2',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='2-я строка'),
        ),
        migrations.AddField(
            model_name='courses',
            name='string_3',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='3-я строка'),
        ),
    ]