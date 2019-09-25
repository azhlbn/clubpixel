from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django import forms

# Create your models here.


class Callbacks(models.Model):
    client_name = models.CharField(max_length=50, verbose_name='Имя клиента')
    client_tel = models.CharField(max_length=50, verbose_name='Номер телефона')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки на звонок'

    def __str__(self):
        return self.client_tel


class Questions(models.Model):
    columns = (
        ('left', 'Левая'),
        ('right', 'Правая'),
    )
    title = models.CharField(max_length=50, verbose_name='Вопрос')
    request_text = models.TextField(verbose_name='Ответ на вопрос')
    column_choice = models.CharField(max_length=30, verbose_name='Выберите колонку', choices=columns)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Ответы на часто задаваемые вопросы'

    def __str__(self):
        return self.title


class Courses(models.Model):
    Yellow = 'Желтый'
    Blue = 'Синий'
    Red = 'Красный'
    colors = ((Yellow, 'Желтый'), (Blue, 'Синий'), (Red, 'Красный'))
    name = models.CharField(max_length=30, verbose_name='Название курса')
    age_min = models.IntegerField(default=None, null=True, verbose_name='Минимальный возраст учеников')
    age_max = models.IntegerField(default=None, null=True, verbose_name='Максимальный возраст учеников')
    string_1 = models.CharField(max_length=100, default=None, null=True, verbose_name='1-я строка')
    string_2 = models.CharField(max_length=100, default=None, null=True, verbose_name='2-я строка')
    string_3 = models.CharField(max_length=100, default=None, null=True, verbose_name='3-я строка')
    btn_color = models.CharField(max_length=50, default=None, null=True, choices=colors, verbose_name='Выберите цвет кнопки')
    bg_image = models.ImageField(upload_to='courses_image', default="default_courses_bg.png", help_text='385 px на 531 px',
                             verbose_name='Фоновое изображение')
    url = models.URLField(verbose_name='Ссылка на подробное описание курса', default=None, null=True)

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name

    def middle_age(self):
        return (self.age_min+self.age_max)/2


class Cities(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название города')
    flag = models.CharField(max_length=30)
    courses = models.ManyToManyField(Courses, verbose_name='Курсы в этом городе', default=None, null=True)
    coords = models.CharField(max_length=100, verbose_name='Координаты', help_text='Для определения координат точки, используйте сервис https://yandex.ru/map-constructor/location-tool/. Пример: [55.4325,37.5498]', default=None, null=True)
    zoom = models.IntegerField(max_length=10, verbose_name='Масштаб', help_text='Можно определить через тот же сервис в поле "Масштаб"', default=None, null=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Documents(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название документа')
    flag = models.CharField(max_length=100, verbose_name='Метка документа', default='None')
    file = models.FileField(verbose_name='Файл')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.title


class Pages(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название страницы')
    link = models.URLField(max_length=100, verbose_name='URL адрес страницы')

    class Meta:
        verbose_name = 'Страницу'
        verbose_name_plural = 'Страницы сайта'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название слайдера', default=None)
    title1 = models.CharField(max_length=60, default='None', verbose_name='Заголовок 1-го слайда', blank=True,
                              help_text='Если заголовок не нужен, оставьте поле пустым')
    button_text1 = models.CharField(max_length=35, default='None', verbose_name='Текст 1-ой кнопки', blank=True,
                                    help_text='Если кнопка не нужна, оставьте поле пустым')
    button_url_1 = models.ForeignKey('Pages', on_delete=models.CASCADE, verbose_name='Ссылка для кнопки', default=None,
                                     null=True, blank=True, related_name='bt_1')
    details_button1_text = models.CharField(max_length=35, null=True, blank=True, verbose_name='Кнопка подробнее')
    details_button1_url = models.URLField(max_length=200, default=None, blank=True, null=True,
                                          verbose_name='Ссылка для кнопки')
    img1 = models.ImageField(upload_to='slider_image', default="default.jpg", help_text='1230 px на 550 px',
                             verbose_name='Изображение 1')

    title2 = models.CharField(max_length=60, null=True, blank=True, verbose_name='Заголовок 2-го слайда')
    button_text2 = models.CharField(max_length=35, null=True, blank=True, verbose_name='Текст 2-ой кнопки')
    button_url_2 = models.ForeignKey('Pages', on_delete=models.CASCADE, verbose_name='Ссылка для кнопки', default=None,
                                     null=True, blank=True, related_name='bt_2')
    details_button2_text = models.CharField(max_length=35, null=True, blank=True, verbose_name='Кнопка подробнее')
    details_button2_url = models.URLField(max_length=200, default=None, blank=True, null=True,
                                          verbose_name='Ссылка для кнопки')
    img2 = models.ImageField(upload_to='slider_image', default="default.jpg", help_text='1230 px на 550 px',
                             verbose_name='Изображение 2', blank=True)

    title3 = models.CharField(max_length=60, null=True, blank=True, verbose_name='Заголовок 3-го слайда')
    button_text3 = models.CharField(max_length=35, null=True, blank=True, verbose_name='Текст 3-ей кнопки')
    button_url_3 = models.ForeignKey('Pages', on_delete=models.CASCADE, verbose_name='Ссылка для кнопки', default=None,
                                     null=True, blank=True, related_name='bt_3')
    details_button3_text = models.CharField(max_length=35, null=True, blank=True, verbose_name='Кнопка подробнее')
    details_button3_url = models.URLField(max_length=200, default=None, blank=True, null=True,
                                          verbose_name='Ссылка для кнопки')
    img3 = models.ImageField(upload_to='slider_image', default="default.jpg", help_text='1230 px на 550 px',
                             verbose_name='Изображение 3', blank=True)


    class Meta:
      verbose_name = 'Слайдер'
      verbose_name_plural = 'Слайдеры'


    def __str__(self):
        return self.title


class BonusModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО контактного лица')
    tel = models.CharField(max_length=30, verbose_name='Номер телефона')
    email = models.EmailField(max_length=30, verbose_name='Email')
    kids_name = models.CharField(max_length=50, verbose_name='ФИО ученика')
    message = models.CharField(max_length=70, verbose_name='Выбранный приз')
    branches = models.CharField(max_length=200, verbose_name='Филиал', null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки', null=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Список заявок на получение приза'


class SeoEngine(models.Model):
    page = models.CharField(max_length=50, verbose_name='Страница')
    title = models.CharField(max_length=300, verbose_name='Заголовок страницы')
    description = models.TextField(max_length=300, verbose_name='Описание страницы')
    keywords = models.CharField(max_length=300, verbose_name='Ключевые слова')

    def get_title(self):
        if self.title:
            return self.title
        return ''

    def get_description(self):
        if self.description:
            return self.description
        return ''

    def get_keywords(self):
        if self.keywords:
            return self.keywords
        return ''

    class Meta:
        verbose_name = 'SEO настройки страницы'
        verbose_name_plural = 'SEO настройки страниц сайта'


class Team(models.Model):
    name_left = models.CharField(max_length=200, verbose_name='Имя сотрудника')
    role_left = models.CharField(max_length=200, verbose_name='Занимаемая должность сотрудника')
    photo_left = models.ImageField(upload_to='team_photos', default="default_photo.jpg", help_text='Размер фото 228x228. Формат PNG. Форма круга с вырезанным фоном',
                             verbose_name='Фото сотрудника')
    name_middle = models.CharField(max_length=200, verbose_name='Имя сотрудника')
    role_middle = models.CharField(max_length=200, verbose_name='Занимаемая должность сотрудника')
    photo_middle = models.ImageField(upload_to='team_photos', default="default_photo.jpg", help_text='Размер фото 228x228. Формат PNG. Форма круга с вырезанным фоном',
                                   verbose_name='Фото сотрудника')
    name_right = models.CharField(max_length=200, verbose_name='Имя сотрудника')
    role_right = models.CharField(max_length=200, verbose_name='Занимаемая должность сотрудника')
    photo_right = models.ImageField(upload_to='team_photos', default="default_photo.jpg", help_text='Размер фото 228x228. Формат PNG. Форма круга с вырезанным фоном',
                                   verbose_name='Фото сотрудника')

    class Meta:
        verbose_name = 'Слайд с сотрудниками'
        verbose_name_plural = 'Команда'


class Feedbacks(models.Model):
    number_of_stars = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    client_name = models.CharField(max_length=200, verbose_name='Имя клиента')
    client_description = models.TextField(verbose_name='Описание клиента')
    feedback_title = models.CharField(max_length=200, verbose_name='Заголовок отзыва')
    feedback_text = models.TextField(verbose_name='Текст отзыва')
    stars = models.IntegerField(choices=number_of_stars, verbose_name='Количество звезд')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')
    client_photo = models.ImageField(upload_to='feedback_clients_photos', default='default-fb-photo.png', verbose_name='Фото клиента')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'