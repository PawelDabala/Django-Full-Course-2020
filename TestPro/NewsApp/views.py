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


def Contact(request):

    return render(request, 'contact.html')
