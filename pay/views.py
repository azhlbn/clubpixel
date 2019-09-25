from django.shortcuts import render, redirect, reverse
from .models import *
from decimal import Decimal
from signup.models import Branches, Franchise
from random import randint
from django.http import Http404, JsonResponse, HttpResponse
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.core import serializers
from .forms import OrderForm
import time
import base64
import hashlib
import json
from pixel.models import Documents, Callbacks, Cities


# Create your views here.


def payment(request):
    city_flag = request.session.get('flag_in_session', False)
    city_products = CityProducts.objects.all()
    franchises = Franchise.objects.all()
    is_franchise = False
    franchise = ''
    for franchise in franchises:
        if str(city_flag) == str(franchise.flag):
            is_franchise = True
            franchise = Franchise.objects.get(flag=city_flag)
    products = []
    for city in city_products: #проходим по уникальным абонементам и ищем совпадение по городу
        if city.product_city.flag == city_flag: #если совпадает flag города в сессии с flag города, выбранного в абонементе, добавляем в список продуктов текущий уникальный абонемент
            products.append(city)

    if len(products) == 0: #если не оказалось уникальных абонементов в текущем городе, добавляем в список продуктов все стандартные абонементы
        products = Products.objects.all()

    try:
        price = Documents.objects.get(flag='price')
    except:
        price = None
    try:
        courses = Documents.objects.get(flag='courses')
    except:
        courses = None
    try:
        techcamp = Documents.objects.get(flag='techcamp')
    except:
        techcamp = None
    try:
        countrycamp = Documents.objects.get(flag='countrycamp')
    except:
        countrycamp = None



    context = {
        'products': products,
        'price': price,
        'courses': courses,
        'techcamp': techcamp,
        'countrycamp': countrycamp,
        'is_franchise': is_franchise,
        'franchise': franchise,
    }

    return render(request, 'pay/payment.html', context)


def product_detail(request, slug):
    try:
        product_detail = CityProducts.objects.get(slug__iexact=slug)
    except CityProducts.DoesNotExist:
        product_detail = Products.objects.get(slug__iexact=slug)

    return render(request, 'pay/product_detail.html', context={'product_detail': product_detail})


def order_details(request, slug):
    current_city = request.session.get('flag_in_session', 'all')
    all_branches = Branches.objects.order_by('-id')
    standart_abons = Products.objects.all()
    uniq_abons = CityProducts.objects.all()
    try:
        doc_courses = Documents.objects.get(flag='courses')
    except:
        doc_courses = None

    #условия при которых осуществляется переадресация при смене города на странице order_details
    city_in_standart_abons = True
    slug_in_standart_abons = False
    session_city_name = ''
    slug_city = ''
    for abon in standart_abons:
        if slug == abon.slug:
            slug_in_standart_abons = True
    for abon in uniq_abons:
        if slug == abon.slug:
            slug_city = str(abon.product_city)
    for abon in uniq_abons:
        try:
            if str(abon.product_city) == str(Cities.objects.get(flag=current_city).name):
                city_in_standart_abons = False
                session_city_name = str(abon.product_city)
        except Cities.DoesNotExist:
            return redirect('/pay/')

    if not city_in_standart_abons and not slug_in_standart_abons and session_city_name == slug_city:
        pass
        # print(f'+ + + не уник слаг и город - принадлежат одному абон - нет переадресации')
    elif not city_in_standart_abons and not slug_in_standart_abons:
        # print(f'+ + + не уник слаг и город - не принадлежат одному абон - переадерсация')
        return redirect('pay.views.product_detail')
    elif city_in_standart_abons and slug_in_standart_abons:
        pass
        # print(f'+ + + слаг и город в стандартных, переадресация не нужна')
    else:
        # print(f'+ + + остальные случаи - переадресация')
        return redirect('/pay/#abonements-anchor')


    try:
        product_detail = CityProducts.objects.get(slug__iexact=slug)
    except CityProducts.DoesNotExist:
        product_detail = Products.objects.get(slug__iexact=slug)
    item_total = product_detail.price

    #делаем список branches из филиалов, которые есть в выбранном (через сессию) городе
    branches = []
    for branch in all_branches:
        if branch.branch_city == Cities.objects.get(flag=current_city):
            branches.append(branch)

    #добавляем переменную для шаблона, по которой можно определить, выбрано "все города" или нет
    all_cities = True
    if current_city != 'all':
        all_cities = False

    if request.method == 'GET':
        form = OrderForm()
    else:
        form = OrderForm(request.POST)
        if form.is_valid():
            form = OrderForm(request.POST)
            if form.is_valid():
                created_order = OrderModel.objects.create(
                    kids_name=form.cleaned_data['kids_name'],
                    birth_date=form.cleaned_data['birth_date'],
                    cost=form.cleaned_data['cost'],
                    abon=form.cleaned_data['abon'],
                    qty=form.cleaned_data['qty'],
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    tel=form.cleaned_data['tel'],
                    branches=form.cleaned_data['branches']
                )
                request.session['order_id'] = created_order.id

            return redirect(formed_order)

    context = {
        'product_detail': product_detail,
        'item_total': item_total,
        'branches': branches,
        'all_cities': all_cities,
        'item_total_2': item_total,
        'doc_courses': doc_courses,
    }


    return render(request, 'pay/order_details.html', context)


def change_item_qty(request):
    coupon_entered = request.GET.get('coupon_entered')
    if coupon_entered == '':
        coupon_entered = 0
    qty = request.GET.get('qty')
    item_slug = request.GET.get('item_slug')
    try:
        item = CityProducts.objects.get(slug=item_slug)
    except CityProducts.DoesNotExist:
        item = Products.objects.get(slug=item_slug)
    coupons = Coupon.objects.all()
    coupon_entered_true = 0
    for coupon in coupons:
        if coupon.discount == int(coupon_entered):
            coupon_entered_true = int(coupon_entered)

    item.item_total = int(qty) * item.price - coupon_entered_true*int(qty)
    if item.item_total <= 0:
        item.item_total = str(item.price)

    context = {
        'item_total': item.item_total,
        'item_total_2': item.item_total,
        'item_qty': qty,
    }

    return JsonResponse(context)


def coupon(request):
    coupon_entered = request.GET.get('coupon_entered')
    item_slug = request.GET.get('item_slug')
    qty = request.GET.get('qty')
    try:
        product_detail = CityProducts.objects.get(slug=item_slug)
    except CityProducts.DoesNotExist:
        product_detail = Products.objects.get(slug=item_slug)

    try:
        coupons = Coupon.objects.get(discount=int(coupon_entered))
        coupon_entered_true = coupons.discount
    except:
        coupon_entered_true = 0

    item_total = product_detail.price*int(qty) - coupon_entered_true*int(qty)
    if item_total <= 0:
        item_total = str(product_detail.price)

    context = {
        'item_total': item_total,
        'item_total_2': item_total,
    }

    return JsonResponse(context)


def formed_order(request):
    # order = OrderModel.objects.order_by('-date')[0]

    order_id = request.session.get('order_id', 1)
    order = OrderModel.objects.get(id=order_id)
    current_time = int(time.time())

    def get_raw_signature(params):
        chunks = []

        for key in sorted(params.keys()):
            if key == 'signature':
                continue

            value = params[key]

            if isinstance(value, str):
                value = value.encode('utf8')
            else:
                value = str(value).encode('utf-8')

            if not value:
                continue

            value_encoded = base64.b64encode(value)
            chunks.append('%s=%s' % (key, value_encoded.decode()))

        raw_signature = '&'.join(chunks)
        return raw_signature

    def double_sha1(secret_key, data):
        sha1_hex = lambda s: hashlib.sha1(s.encode('utf-8')).hexdigest()
        digest = sha1_hex(secret_key + sha1_hex(secret_key + data))
        return digest

    def get_signature(secret_key: str, params: dict) -> str:
        return double_sha1(secret_key, get_raw_signature(params))

    price = int()
    try:
        price = int(order.cost.split(',')[0])
    except:
        price = int(order.cost.split('.')[0])

    check_items = {
         "name": "Абонемент на посещение занятий по робототехники",
         "quantity": 1,
         "price": price,
         "sno": "usn_income",
         "payment_object": "service",
         "payment_method": "full_prepayment",
         "vat": "none",
    }

    receipt_items = json.dumps(check_items)

    order_items = {
        "testing": "0",
        "order_id": order.id,
        "amount": order.cost,
        "merchant": "a646bf9f-447a-4a75-8d0c-c59c2e8efb32",
        "description": "Заказ №" + str(order.id),
        "receipt_contact": order.email,
        "receipt_items": receipt_items,
        "client_phone": order.tel,
        "client_email": order.email,
        "client_name": order.name,
        "success_url": "https://docs.google.com/forms/d/e/1FAIpQLSegmLhK-RzWohvFv87S1RCjtr-Uur7-idufr6OLoH3KX83eww/viewform",
        "fail_url": "https://pay.modulbank.ru/fail",
        "unix_timestamp": current_time,
    }

    signature = get_signature('1044928D536800D86B81F988D2A06C8F', order_items)

    context = {
        'order': order,
        'current_time': current_time,
        'signature': signature,
        'receipt_items': receipt_items,
    }

    return render(request, 'pay/formed_order.html', context)


# def order_create(request, slug):
#     qty = request.GET.get('qty')
#     kids_name = request.GET.get('kids_name')
#     name = request.GET.get('n')
#     email = request.GET.get('email')
#     tel = request.GET.get('tel')
#     branches = request.GET.get('branches')
#     coupon_entered = request.GET.get('coupon_entered')
#     birth_date = request.GET.get('birth_date')
#     abon = request.GET.get('abon')
#
#     try:
#         product_detail = CityProducts.objects.get(slug=slug)
#     except CityProducts.DoesNotExist:
#         product_detail = Products.objects.get(slug=slug)
#
#     if coupon_entered != '':
#         try:
#             coupons = Coupon.objects.get(discount=int(coupon_entered))
#             coupon_entered_true = coupons.discount
#         except:
#             coupon_entered_true = 0
#         cost = product_detail.price*int(qty) - int(coupon_entered_true)*int(qty)
#         if cost <= 0:
#             cost = product_detail.price
#     else:
#         cost = str(product_detail.price*int(qty))
#
#     created_order = OrderModel.objects.create(kids_name=kids_name, cost=cost, qty=qty, name=name, email=email, tel=tel, branches=branches, birth_date=birth_date, abon=abon)
#     request.session['order_id'] = created_order.id
#
#     return HttpResponse()