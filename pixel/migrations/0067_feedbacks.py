# Generated by Django 2.2.1 on 2019-09-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0066_auto_20190916_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200, verbose_name='Имя клиента')),
                ('client_description', models.TextField(verbose_name='Описание клиента')),
                ('feedback_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('feedback_text', models.TextField(verbose_name='Текст')),
                ('stars', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Количество звезд')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')),
                ('client_photo', models.ImageField(default='default_client_photo.jpg', upload_to='feedback_clients_photos', verbose_name='Фото клиента')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
