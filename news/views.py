from django.shortcuts import render
from .models import News
# Create your views here.


def news_list(request):
    news_all = News.objects.all().order_by('-date')
    return render(request, 'news/news_list.html', {'news_all': news_all})


def news_detail(request, slug):
    news_single = News.objects.get(slug=slug)
    news_all = News.objects.all().order_by('-date')
    news_last = News.objects.order_by('-date')[0:3]
    return render(request, 'news/news_detail.html', {'news_single': news_single, 'news_all': news_all, 'news_last': news_last})
