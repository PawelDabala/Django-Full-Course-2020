from django.shortcuts import render, HttpResponse
from .models import News, SportNews

# 138:51

# Create your views here.


def Home(request):
    context = {
        "name": "Pawel Dabala",
        "number": 213432
    }
    return render(request, 'index.html', context)


def NewsP(request):

    obj = News.objects.get(id=1)

    context = {
        'data': obj
    }
    return render(request, 'news.html', context=context)


def NewsDate(request, year):

    artical_list = News.objects.filter(pub_date__year=year)

    context = {
        'year': year,
        'artical_list': artical_list
    }
    return render(request, 'newsdate.html', context)


def Contact(request):
    return render(request, 'contact.html')
