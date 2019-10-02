from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail, BadHeaderError
from signup.models import Branches
from .forms import BonusForm, SignupForm
from pixelproject import settings
from signup.models import SignupModel, Franchise
from news.models import News
from django.core.paginator import Paginator
import json
from el_pagination.decorators import page_template

# Create your views here.


def age_range(request, min_age, max_age):
    request.session['min_age'] = min_age
    request.session['max_age'] = max_age
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def session_reset(request):
    request.session['flag_in_session'] = False
    request.session['min_age'] = 5
    request.session['max_age'] = 15
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def set_city(request, city_flag):
    request.session['flag_in_session'] = city_flag
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@page_template('pixel/desktop_courses.html', key='desktop_courses')
@page_template('pixel/mobile_courses.html', key='mobile_courses')


def main(request, template='pixel/main.html', extra_context=None):
    city_flag = request.session.get('flag_in_session', False)
    created_signup_model = '' #empty model
    last_news_1 = News.objects.order_by('-date')[0]
    last_news_2 = News.objects.order_by('-date')[1]
    last_news_3 = News.objects.order_by('-date')[2]
    if request.method == 'GET':
        form = SignupForm()
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            form = SignupForm(request.POST)
            if form.is_valid():
                email_subject = 'CLUBPIXEL.RU :: Запись на занятие '
                email_body = "С сайта clubpixel.ru отправлено новое сообщение\n\n" \
                             "ФИО контактного лица: %s \n" \
                             "Телефон: %s \n" \
                             "Email: %s \n" \
                             "ФИО ученика: %s \n" \
                             "Дата рождения ученика: %s \n" \
                             "Филиал: %s \n\n" \
                             "Услуга: \n" \
                             "%s " % \
                             (form.cleaned_data['name'], form.cleaned_data['tel'], form.cleaned_data['email'],
                              form.cleaned_data['kid_name'], form.cleaned_data['kid_age'],
                              form.cleaned_data['branches'], form.cleaned_data['service'])

                # Положим копию письма в базу данных
                created_signup_model = SignupModel.objects.create(name=form.cleaned_data['name'],
                                           tel=form.cleaned_data['tel'], email=form.cleaned_data['email'],
                                           kid_name=form.cleaned_data['kid_name'], kid_age=form.cleaned_data['kid_age'],branches=form.cleaned_data['branches'],
                                           service=form.cleaned_data['service'])

            try:
                for franchise in Franchise.objects.all():
                    if created_signup_model.branches == franchise.adr:
                        send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['bordikvg@clubpixel.ru'],
                                  fail_silently=False)
                        send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, [franchise.email],
                                  fail_silently=False)
                        break
                    else:
                        send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['bordikvg@clubpixel.ru'],
                                  fail_silently=False)
                        send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['info@clubpixel.ru'],
                                  fail_silently=False)
                        send_mail(email_subject, email_body, settings.EMAIL_HOST_USER,
                                  ['17192671.203237@parser.amocrm.ru'],
                                  fail_silently=False)
                        break

            except BadHeaderError:
                return HttpResponse('Ошибка отправки формы')
            return redirect('signup_thx')

    slider = Slider.objects.get()
    questions = Questions.objects.all()
    branches = Branches.objects.all()
    franchises = Franchise.objects.all()
    courses = Courses.objects.all().order_by('age_min')

    min_age = int(request.session.get('min_age', 5))
    max_age = int(request.session.get('max_age', 15))

    try:
        if city_flag and city_flag != 'favicon.ico' and city_flag is not None:
            city = Cities.objects.get(flag=city_flag)
        else:
            try:
                city = Franchise.objects.get(flag=city_flag)
            except:
                city = Cities.objects.get(flag='all')
    except:
        try:
            city = Franchise.objects.get(flag=city_flag)
        except:
            city = Cities.objects.get(flag='all')


    # создаю список курсов, которые есть в городе из сессии
    courses_list = []
    for course in city.courses.all():
        courses_list.append(str(course))

    # создаю словарь филиалов, находящихся в городе city с чередованием цветов иконок

    branches_in_city = dict()
    if city.flag != 'all':
        for branch in branches:
            if branch.branch_city == city:
                branches_in_city[branch] = ''
        for branch in franchises:
            if str(branch.name) == str(city):
                branches_in_city[branch] = ''
    else:
        for branch in branches:
            branches_in_city[branch] = ''
        for branch in franchises:
            branches_in_city[branch] = ''

    color = 'blue'
    for branch in branches_in_city:
        if color == 'blue':
            branches_in_city[branch] = 'blue'
            color = 'white'
        else:
            branches_in_city[branch] = 'white'
            color = 'blue'

    # создаю весь список филиалов с чередованием по цветам иконок
    all_branches = dict()
    color = 'blue'
    for branch in branches:
        if color == 'blue':
            all_branches[branch] = 'blue'
            color = 'white'
        else:
            all_branches[branch] = 'white'
            color = 'blue'


    branches_and_franchises = [branch for branch in branches]
    for franchise in franchises:
        branches_and_franchises.append(franchise)

    if Team.objects.all():
        first_team_slide = Team.objects.all()[0]
        team_slides = Team.objects.all()[1:]
        all_team_members = []
        for slide in Team.objects.all():
            all_team_members.append(
                [slide.name_left, slide.role_left, slide.photo_left, '/static/img/team-member-1-bg.png'])
            all_team_members.append(
                [slide.name_middle, slide.role_middle, slide.photo_middle, '/static/img/team-member-2-bg.png'])
            all_team_members.append(
                [slide.name_right, slide.role_right, slide.photo_right, '/static/img/team-member-3-bg.png'])
    else:
        all_team_members = ''
        team_slides = ''
        first_team_slide = ''


    all_fb = Feedbacks.objects.all()
    fb_list = []
    fb_trio = []
    for fb in all_fb[3:]:
        fb_trio.append(fb)
        if len(fb_trio) == 3:
            fb_list.append(fb_trio)
            fb_trio = []
        elif fb == all_fb.order_by('-date')[0]:
            while len(fb_trio) != 3:
                fb_trio.append('')
            fb_list.append(fb_trio)

    try:
        fb1 = all_fb[0]
    except:
        fb1 = ''
    try:
        fb2 = all_fb[1]
    except:
        fb2 = ''
    try:
        fb3 = all_fb[2]
    except:
        fb3 = ''

    # if request.is_ajax():
    #     template = desktop_courses

    filtered_list_of_courses = []
    filtered_list_of_mobile_courses = []
    for course in courses:
        if course.age_min <= max_age and course.age_max >= min_age and course.name in courses_list:
            filtered_list_of_courses.append(course)
            filtered_list_of_mobile_courses.append(course)

    context = {
        'slider': slider,
        'min_age': min_age,
        'max_age': max_age,
        'questions': questions,
        'branches': branches,
        'city': city,
        'city_flag': city_flag,
        'branches_in_city': branches_in_city,
        'all_branches': all_branches,
        'courses': filtered_list_of_courses,
        'mobile_courses_list': filtered_list_of_mobile_courses,
        'courses_list': courses_list,
        'branches_and_franchises': branches_and_franchises,
        'last_news_1': last_news_1,
        'last_news_2': last_news_2,
        'last_news_3': last_news_3,
        'team_slides': team_slides,
        'first_team_slide': first_team_slide,
        'all_team_members': all_team_members[1:],
        'fb1': fb1,
        'fb2': fb2,
        'fb3': fb3,
        'all_fb': fb_list,
        'mobile_courses': 'pixel/mobile_courses.html',
        'desktop_courses': 'pixel/desktop_courses.html',
    }

    if extra_context is not None:
        context.update(extra_context)

    return render(request, template, context)


# def mobile_courses(request, template='pixel/mobile_courses.html', extra_context=None):
#     courses = Courses.objects.all().order_by('age_min')
#     city_flag = request.session.get('flag_in_session', False)
#     min_age = int(request.session.get('min_age', 5))
#     max_age = int(request.session.get('max_age', 15))
#
#     try:
#         if city_flag and city_flag != 'favicon.ico' and city_flag is not None:
#             city = Cities.objects.get(flag=city_flag)
#         else:
#             try:
#                 city = Franchise.objects.get(flag=city_flag)
#             except:
#                 city = Cities.objects.get(flag='all')
#     except:
#         try:
#             city = Franchise.objects.get(flag=city_flag)
#         except:
#             city = Cities.objects.get(flag='all')
#
#     courses_list = []
#     for course in city.courses.all():
#         courses_list.append(str(course))
#
#     filtered_list_of_courses = []
#     for course in courses:
#         if course.age_min <= max_age and course.age_max >= min_age and course.name in courses_list:
#             filtered_list_of_courses.append(course)
#
#     context = {
#         'courses': filtered_list_of_courses,
#     }
#
#     if extra_context is not None:
#         context.update(extra_context)
#
#     return render(request, template, context)


def sports_group(request):
    return render(request, 'pixel/sports_group.html')


def contract_courses(request):
    return render(request, 'pixel/contract_courses.html')


def price(request):
    return render(request, 'pixel/price.html')


def contract_techcamp(request):
    return render(request, 'pixel/contract_techcamp.html')


def signup_thx(request):
    return render(request, 'pixel/signup_thx.html')


def listok_lk(request):
    return render(request, 'pixel/listok_lk.html')


def courses(request):
    return render(request, 'pixel/courses.html')


def franchise(request):
    return render(request, 'pixel/franchise.html')

def summer(request):
    return render(request, 'pixel/summer.html')


def bonus(request):
    branches = Branches.objects.all()
    if request.method == 'GET':
        form = BonusForm()
    else:
        form = BonusForm(request.POST)
        if form.is_valid():

            email_subject = 'CLUBPIXEL.RU – ПиксельБонус'
            email_body = "С сайта clubpixel.ru отправлено новое сообщение\n\n" \
                         "ФИО контактного лица: %s \n" \
                         "Номер телефона: %s \n" \
                         "ФИО ребенка: %s \n" \
                         "Филиал: %s \n" \
                         "E-mail отправителя: %s \n\n" \
                         "Выбранный приз: \n" \
                         "%s " % \
                         (form.cleaned_data['name'], form.cleaned_data['tel'], form.cleaned_data['kids_name'], form.cleaned_data['branches'], form.cleaned_data['email'], form.cleaned_data['message'])

            # Положим копию письма в базу данных
            BonusModel.objects.create(name=form.cleaned_data['name'], tel=form.cleaned_data['tel'], email=form.cleaned_data['email'], kids_name=form.cleaned_data['kids_name'], message=form.cleaned_data['message'], branches=form.cleaned_data['branches'])

        try:
            send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['info@clubpixel.ru'], fail_silently=False)
            send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['zubkovas@clubpixel.ru'], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('bonus_thx')
    return render(request, 'pixel/bonus.html', {'form': form, 'branches': branches})


def bonus_thx(request):
    return render(request, 'pixel/bonus_thx.html')


def successView(request):
    return render(request, 'signup/signup_thx.html')


def kinder(request):
    return render(request, 'pixel/kinder.html')


def wedo(request):
    return render(request, 'pixel/wedo.html')


def scratch(request):
    return render(request, 'pixel/scratch.html')


def mindstorms(request):
    return render(request, 'pixel/mindstorms.html')


def mindstormspro(request):
    return render(request, 'pixel/mindstormspro.html')


def arduino(request):
    return render(request, 'pixel/arduino.html')


def table(request):
    return render(request, 'pixel/table.html')


def franchise_form(request):
    return render(request, 'pixel/franchise_form.html')

def license(request):
    return render(request, 'pixel/license.html')


def intense(request):
    return render(request, 'pixel/intense.html')


def policy(request):
    return render(request, 'pixel/policy.html')


def leto(request):
    return render(request, 'pixel/leto.html')


def galery(request):
    context = {
        'insta_items': insta_items,
    }
    return render(request, 'pixel/galery.html', context)


def serpuhov(request):
    return render(request, 'pixel/serpuhov.html')


def domodedovo(request):
    return render(request, 'pixel/domodedovo.html')


def step(request):
    return render(request, 'pixel/step.html')


def metro_uj(request):
    return render(request, 'pixel/metro_u.html')


def insta_details(request, id):
    for i in range(len(insta_items_details)):
        if id in insta_items_details[i]:
            post = insta_items_details[i]
            if i == len(insta_items_details)-1:
                next_post = None
            else:
                next_post = insta_items_details[i+1]
            if i == 0:
                prev_post = None
            else:
                prev_post = insta_items_details[i-1]
    url = post[0]
    text = post[1]
    likes = post[3]
    comments = post[2]
    comments_list = post[6]
    days_from_post = post[7]
    link = post[4]
    if next_post:
        next_id = next_post[5]
    else:
        next_id = False
    if prev_post:
        prev_id = prev_post[5]
    else:
        prev_id = False

    context = {
        'url': url,
        'text': text,
        'next_id': next_id,
        'prev_id': prev_id,
        'comments_list': comments_list,
        'likes': likes,
        'comments': comments,
        'days_from_post': days_from_post,
        'link': link,
    }

    return render(request, 'pixel/insta_details.html', context)


def summ_courses(request):
    return render(request, 'pixel/summ_courses.html')


def callback(request):
    if request.GET:
        client_name = request.GET['client_name']
        client_tel = request.GET['client_tel']
        client_check = request.GET['client_check']
        if client_name and client_tel and client_check == 'true':
            Callbacks.objects.create(client_name=client_name, client_tel=client_tel)
            email_subject = 'CLUBPIXEL.RU - Обратный звонок'
            email_body = f'С сайта clubpixel.ru получена заявка на обратный звонок \n\n \
Имя клиента: {client_name} \n \
Номер телефона: {client_tel}'

            try:
                send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['bordikvg@clubpixel.ru'],
                          fail_silently=False)
                send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['info@clubpixel.ru'],
                          fail_silently=False)
                send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['azhlbn@gmail.com'],
                          fail_silently=False)
            except BadHeaderError:
                pass
            return HttpResponse('Success')
        else:
            return HttpResponse('Fail')


def minecraft(request):
    return render(request, 'pixel/minecraft.html')


def kodu(request):
    return render(request, 'pixel/kodu.html')


def unity3d(request):
    return render(request, 'pixel/unity3d.html')


def team(request):
    all_slides = Team.objects.all()
    all_team_members = []
    for slide in all_slides:
        all_team_members.append([slide.name_left, slide.role_left, slide.photo_left, '/static/img/team-member-1-bg.png'])
        all_team_members.append([slide.name_middle, slide.role_middle, slide.photo_middle, '/static/img/team-member-2-bg.png'])
        all_team_members.append([slide.name_right, slide.role_right, slide.photo_right, '/static/img/team-member-3-bg.png'])

    context = {
        'all_team_members': all_team_members,
    }
    return render(request, 'pixel/team.html', context)