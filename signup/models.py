from django.db import models
from pixel.models import Cities, Courses
from ckeditor.fields import RichTextField

# Create your models here.

class SignupModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО контактного лица')
    tel = models.CharField(max_length=200, verbose_name='Номер телефона')
    email = models.CharField(max_length=200, verbose_name='Email')
    kid_name = models.CharField(max_length=200, verbose_name='ФИО ученика')
    kid_age = models.CharField(max_length=200, verbose_name='Дата рождения ученика')
    branches = models.CharField(max_length=200, verbose_name='Филиал', null=True)
    service = models.CharField(max_length=200, default='Запись на пробное занятие', verbose_name='Услуга')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки', null=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Branches (models.Model):
    name = models.CharField(max_length=100, verbose_name='Название филиала')
    adr = models.CharField(max_length=100, verbose_name='Адрес филиала')
    yandex_adr = models.CharField(max_length=100, verbose_name='Адрес филила для Яндекса', help_text='Точный адрес для поиска здания на картах Яндекса')
    branch_city = models.ForeignKey(Cities, verbose_name='Город, в котором находится филиал', on_delete=models.CASCADE, default=None, null=True)
    description_url = models.URLField(verbose_name='Ссылка внутри метки на карте', default=None, null=True)

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return self.name


class Franchise(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    tel = models.CharField(max_length=100, verbose_name='Телефон', help_text='Правильный формат: +7 (999) 111 22 33')
    email = models.CharField(max_length=100, verbose_name='Почта, на которую будут приходить заявки')
    adr = models.CharField(max_length=200, verbose_name='Адрес')
    courses = models.ManyToManyField(Courses, verbose_name='Курсы в этом филиале')
    coords = models.CharField(max_length=100, verbose_name='Координаты', help_text='Для определения координат точки, используйте сервис https://yandex.ru/map-constructor/location-tool/. Пример: [55.4325,37.5498]')
    zoom = models.IntegerField(max_length=10, verbose_name='Масштаб', help_text='Можно определить через тот же сервис в поле "Масштаб"')
    yandex_adr = models.CharField(max_length=100, verbose_name='Адрес филила для Яндекса', help_text='Точный адрес для поиска здания на картах Яндекса')
    description_url = models.URLField(verbose_name='Ссылка внутри метки на карте')
    flag = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Франшиза'
        verbose_name_plural = 'Франшизы'

    def __str__(self):
        return self.name