from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Slider)
admin.site.register(Pages)
admin.site.register(Documents)
admin.site.register(Questions)


class BonusAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')


class CallbacksAdmin(admin.ModelAdmin):
    list_display = ('client_tel', 'client_name', 'date')


admin.site.register(Callbacks, CallbacksAdmin)
admin.site.register(BonusModel, BonusAdmin)


class CitiesAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'flag', 'courses')
        }),
        # ('Выберите какие курсы доступны в этом городе', {
        #     'fields': ('kinder', 'wedo', 'scratch', 'mindstorms', 'mindstormspro', 'arduino', 'leto_wedo', 'leto_mindstorms', 'minecraft', 'kodu', 'unity3d')
        # }),
        ('Координаты центрирования Яндекс карт, при выборе города и масштабирование', {
            'fields': ('coords', 'zoom')
        }),
    )


admin.site.register(Cities, CitiesAdmin)


class CoursesAdmin(admin.ModelAdmin):
    ordering = ('age_min',)


admin.site.register(Courses, CoursesAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_left', 'name_middle', 'name_right')
    fieldsets = (
        ('Первый струдник', {
            'fields': ('name_left', 'role_left', 'photo_left')
        }),
        ('Второй сотрудник', {
            'fields': ('name_middle', 'role_middle', 'photo_middle')
        }),
        ('Третий сотрудник', {
            'fields': ('name_right', 'role_right', 'photo_right')
        }),
    )


admin.site.register(Team, TeamAdmin)


class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'date')


admin.site.register(Feedbacks, FeedbacksAdmin)
