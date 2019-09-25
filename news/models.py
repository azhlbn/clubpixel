from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=60, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='URL новости', help_text='Латинские буквы и символы "-" и "_". Без пробелов')
    body = RichTextField(default=None, verbose_name='Содержание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    thumb = models.ImageField(default='/static/img/default.jpg', blank=True)
    # author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:200] + '...'

    def snippet_short(self):
        return self.body[:150] + '...'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
