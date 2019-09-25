# Generated by Django 2.1.3 on 2019-02-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0002_auto_20190213_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='full_img',
            field=models.ImageField(blank=True, default='product_default.jpg', help_text='Необязательное поле', upload_to='products_image', verbose_name='Изображение в описании'),
        ),
        migrations.AlterField(
            model_name='products',
            name='img',
            field=models.ImageField(blank=True, default='product_default.jpg', help_text='Необязательное поле', upload_to='products_image', verbose_name='Фоновое изображение'),
        ),
    ]