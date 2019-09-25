from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'pixel'

urlpatterns = [
    path('', main, name='main'),
    path('sports_group/', sports_group, name='sports_group'),
    path('contract-courses', contract_courses, name='contract_courses'),
    path('price', price, name='price'),
    path('contract-techcamp', contract_techcamp, name='contract-techcamp'),
    path('lk', listok_lk, name='listok_lk'),
    path('kursy', courses, name='courses'),
    path('franshiza', franchise, name='franchise'),
    path('summer', summer, name='summer'),
    path('bonus', bonus, name='bonus'),
    path('kinder', kinder, name='kinder'),
    path('wedo', wedo, name='wedo'),
    path('scratch', scratch, name='scratch'),
    path('mindstorms', mindstorms, name='mindstorms'),
    path('mindstormspro', mindstormspro, name='mindstormspro'),
    path('arduino', arduino, name='arduino'),
    path('raspisanie', table, name='table'),
    path('zapis-franshiza', franchise_form, name='franchise_form'),
    path('license', license, name='license'),
    path('intensiv', intense, name='intense'),
    path('politika', policy, name='policy'),
    path('bonus_thx', bonus_thx, name='bonus_thx'),
    path('leto', leto, name='leto'),
    path('s', serpuhov, name='serpuhov'),
    path('d', domodedovo, name='domodedovo'),
    path('step', step, name='step'),
    path('u', metro_uj, name='metro_uj'),
    path('leto-kursy', summ_courses, name='summ_courses'),
    path('set_city/<city_flag>', set_city, name='set_city'),
    path('session/reset', session_reset, name='session_reset'),
    path('age_range/<min_age>-<max_age>', age_range, name='age_range'),
    path('callback', callback, name='callback'),
    path('minecraft', minecraft, name='minecraft'),
    path('kodu', kodu, name='kodu'),
    path('unity3d', unity3d, name='unity3d'),
    path('team', team, name='team'),
]
