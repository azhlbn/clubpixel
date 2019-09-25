from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# from .forms import SignupForm
from pixelproject import settings
from .models import *


def emailView(request):
    branches = Branches.objects.all()
    if request.method == 'GET':
        form = SignupForm()
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # surname = form.cleaned_data['surname']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']

            email_subject = 'CLUBPIXEL.RU :: Запись на занятие '
            email_body = "С сайта clubpixel.ru отправлено новое сообщение\n\n" \
                         "Имя отправителя: %s \n" \
                         "Фамилия отправителя: %s \n" \
                         "Контактный телефон: %s \n" \
                         "Фамилия и имя ребенка: %s \n" \
                         "Возраст ребенка: %s \n" \
                         "Филиал: %s \n" \
                         "E-mail отправителя: %s \n\n" \
                         "Дополнительно: \n" \
                         "%s " % \
                         (form.cleaned_data['name'], form.cleaned_data['surname'], form.cleaned_data['tel'], form.cleaned_data['kid_name'], form.cleaned_data['kid_age'], form.cleaned_data['branches'], form.cleaned_data['email'], form.cleaned_data['message'])

            # Положим копию письма в базу данных
            SignupModel.objects.create(name=form.cleaned_data['name'], surname=form.cleaned_data['surname'], tel=form.cleaned_data['tel'], kid_name=form.cleaned_data['kid_name'], kid_age=form.cleaned_data['kid_age'], branches=form.cleaned_data['branches'], email=form.cleaned_data['email'], message=form.cleaned_data['message'])

        try:
            send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['azhlbn@yandex.ru'], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('signup_thx')
    return render(request, 'signup/signup.html', {'form': form, 'branches': branches})

def successView(request):
    return render(request, 'signup/signup_thx.html')
