from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Branches)


class SignupAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'date')


admin.site.register(SignupModel, SignupAdmin)


class FranchiseAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'tel', 'email', 'adr', 'courses')
        }),
        # ('Выберите какие курсы доступны в этом городе', {
        #     'fields': ('kinder', 'wedo', 'scratch', 'mindstorms', 'mindstormspro', 'arduino', 'leto_wedo', 'leto_mindstorms', 'minecraft', 'kodu', 'unity3d')
        # }),
        ('Настройки для отображения филиала на Яндекс-картах', {
            'fields': ('coords', 'zoom', 'yandex_adr', 'description_url')
        }),
        ('Техническая информация', {
            'fields': ('flag',)
        }),
    )
    prepopulated_fields = {'flag': ('name',)}


admin.site.register(Franchise, FranchiseAdmin)