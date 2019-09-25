from django.contrib import admin
from .models import *

# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CityProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)+('price',)+('product_city',)}
    list_display = ('name', 'product_city')


admin.site.register(Products, ProductsAdmin)
admin.site.register(CityProducts, CityProductsAdmin)
admin.site.register(Coupon)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('kids_name', 'name', 'date')


admin.site.register(OrderModel, OrderAdmin)
