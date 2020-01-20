from django.shortcuts import render, HttpResponse


# Create your views here.
def Home(request):
    return render(request, 'index.html')


def News(request):
    return render(request, 'news.html')


def Contact(request):
    return render(request, 'contact.html')
