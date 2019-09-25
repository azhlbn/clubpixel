from django.db import models
from ckeditor.fields import RichTextField
from pixel.models import Cities
from decimal import Decimal
from django.template.defaultfilters import truncatechars

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=40, default=None, verbose_name='Название абонемента')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL страницы', default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None, verbose_name='Цена абонемента')
    crossed_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None, blank=True, verbose_name='Зачеркнутая цена абонемента')
    # product_city = models.ForeignKey(Cities, on_delete=models.CASCADE(), default='Все города', verbose_name='Город абонемента')
    body = RichTextField(default=None, verbose_name='Описание абонемента')
    img = models.ImageField(upload_to='products_image', default='pay-detail-img.jpg', verbose_name='Фоновое изображение', help_text='Необязательное поле', blank=True)
    full_img = models.ImageField(upload_to='products_image', default='pay-detail-img.jpg', verbose_name='Изображение в описании', help_text='Необязательное поле', blank=True)
    qty = models.PositiveIntegerField(default=1, editable=False)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, editable=False)

    # def get_absolute_url(self):
    #     return reverse('product_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Общие абонементы'

    def __str__(self):
        return self.name


class CityProducts(models.Model):
    name = models.CharField(max_length=40, default=None, verbose_name='Название абонемента')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None, verbose_name='Цена абонемента')
    crossed_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None, blank=True, verbose_name='Зачеркнутая цена абонемента')
    product_city = models.ForeignKey(Cities, on_delete=models.CASCADE, default='Город не выбран', verbose_name='Город абонемента')
    body = RichTextField(default=None, verbose_name='Описание абонемента')
    img = models.ImageField(upload_to='products_image', default='pay-detail-img.jpg', verbose_name='Фоновое изображение', help_text='Необязательное поле', blank=True)
    full_img = models.ImageField(upload_to='products_image', default='pay-detail-img.jpg', verbose_name='Изображение в описании', help_text='Необязательное поле', blank=True)
    qty = models.PositiveIntegerField(default=1, editable=False)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, editable=False)
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL страницы (автозаполнение)', default=None)
    # def get_absolute_url(self):
    #     return reverse('product_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Уникальные абонементы'

    def __str__(self):
        return self.name


class Coupon(models.Model):
    name = models.CharField(max_length=40, default=None, verbose_name='Название купона')
    discount = models.PositiveIntegerField(default=None, verbose_name='Размер скидки')
    description = models.TextField(verbose_name='Описание купона', blank=True)

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    kids_name = models.CharField(max_length=30, default=None, verbose_name='ФИО ученика')
    birth_date = models.CharField(max_length=30, default='Не указано', verbose_name='Дата рождения')
    cost = models.CharField(max_length=20, default=None, verbose_name='Сумма покупки', null=True)
    abon = models.CharField(max_length=30, default='Не указано', verbose_name='Тип абонемента', null=True)
    qty = models.CharField(max_length=20, default=None, verbose_name='Количество абонементов', null=True)
    name = models.CharField(max_length=30, default=None, verbose_name='ФИО плательщика', null=True)
    email = models.CharField(max_length=30, default=None, verbose_name='Email', null=True)
    tel = models.CharField(max_length=30, default=None, verbose_name='Номер телефона', null=True)
    branches = models.CharField(max_length=200, verbose_name='Филиал', null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.kids_name

    def get_absolute_url(self):
        return "/formed_order/%s" % (self.date.strftime('%Y%m%d') + '-' + str(self.id))
