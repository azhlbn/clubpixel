# Generated by Django 2.1.2 on 2018-11-13 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название страницы')),
                ('link', models.URLField(max_length=100, verbose_name='URL адрес страницы')),
            ],
            options={
                'verbose_name': 'Страницу',
                'verbose_name_plural': 'Страницы сайта',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=40, verbose_name='Название абонемента')),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=10, verbose_name='Цена абонемента')),
                ('img', models.ImageField(blank=True, default='product_default.jpg', help_text='Необязательное поле', upload_to='products_image', verbose_name='Фоновая картинка')),
            ],
            options={
                'verbose_name': 'Абонемент',
                'verbose_name_plural': 'Абонементы',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=40, verbose_name='Название слайдера')),
                ('title1', models.CharField(blank=True, default='None', help_text='Если заголовок не нужен, оставьте поле пустым', max_length=40, verbose_name='Заголовок 1-го слайда')),
                ('button_text1', models.CharField(blank=True, default='None', help_text='Если кнопка не нужна, оставьте поле пустым', max_length=35, verbose_name='Текст 1-ой кнопки')),
                ('img1', models.ImageField(default='default.jpg', help_text='1230 px на 550 px', upload_to='slider_image', verbose_name='Изображение 1')),
                ('title2', models.CharField(blank=True, max_length=40, null=True, verbose_name='Заголовок 2-го слайда')),
                ('button_text2', models.CharField(blank=True, max_length=35, null=True, verbose_name='Текст 2-ой кнопки')),
                ('img2', models.ImageField(blank=True, default='default.jpg', help_text='1230 px на 550 px', upload_to='slider_image', verbose_name='Изображение 2')),
                ('title3', models.CharField(blank=True, max_length=40, null=True, verbose_name='Заголовок 3-го слайда')),
                ('button_text3', models.CharField(blank=True, max_length=35, null=True, verbose_name='Текст 3-ей кнопки')),
                ('img3', models.ImageField(blank=True, default='default.jpg', help_text='1230 px на 550 px', upload_to='slider_image', verbose_name='Изображение 3')),
                ('button_url_1', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bt_1', to='pixel.Pages', verbose_name='Ссылка для кнопки')),
                ('button_url_2', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bt_2', to='pixel.Pages', verbose_name='Ссылка для кнопки')),
                ('button_url_3', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bt_3', to='pixel.Pages', verbose_name='Ссылка для кнопки')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдеры',
            },
        ),
    ]