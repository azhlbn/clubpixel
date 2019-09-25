from . import views
from django.urls import path
from django.conf.urls import url
from pixel.views import callback

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news'),
    path('<str:slug>/', views.news_detail, name='detail'),
    path('callback', callback, name='callback'),
]