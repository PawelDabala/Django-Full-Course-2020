from django.shortcuts import render, HttpResponse
from .models import News


# Create your views here.
def Home(request):

    context = {
        "name": 'Pawel',
        "number": 10000
    }

    return render(request, 'index.html', context=context)


def NewsP(request):

    obj = News.objects.get(id=1)
    context = {
        "data": obj
    }
    return render(request, 'news.html', context=context)


def NewsDate(request, year):
    article_list = News.objects.filter(pub_date__year=year)

    context = {
        'year': year,
        'article_list': article_list
    }
    return render(request, 'newsdate.html', context)


def Contact(request):

    return render(request, 'contact.html')
