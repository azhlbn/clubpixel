# Generated by Django 2.2.1 on 2019-09-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0073_auto_20190923_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='client_photo',
            field=models.ImageField(default='default-fb-photo.png', help_text='Изображение должно быть круглым с вырезанным фоном', upload_to='feedback_clients_photos', verbose_name='Фото клиента'),
        ),
    ]
