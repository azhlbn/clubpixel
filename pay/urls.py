from django.urls import path
from .views import *
from pixel.views import callback
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('product_detail/<str:slug>/', product_detail, name='product_detail'),
    path('', payment, name='payment'),
    path('order_details/<str:slug>/', order_details, name='order_details'),
    path('change_item_qty/', change_item_qty, name='change_item_qty'),
    path('coupon/', coupon, name='coupon'),
    path('formed_order/', formed_order, name='formed_order'),
    # path('order_create/<str:slug>/', order_create, name='order_create'),
    path('callback', callback, name='callback'),
]