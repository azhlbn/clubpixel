from django.urls import path
from .views import galery, insta_details
from pixel.views import callback


urlpatterns = [
    path('', galery, name='galery'),
    path('details/<id>/', insta_details, name='insta_details'),
    path('callback', callback, name='callback'),
]