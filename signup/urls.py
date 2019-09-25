from django.contrib import admin
from django.urls import path
from .views import *
from pixel.views import callback

urlpatterns = [
    path('', emailView, name='signup'),
    path('signup_thx/', successView, name='signup_thx'),
    path('callback', callback, name='callback'),
]