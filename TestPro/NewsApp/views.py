from django.shortcuts import render, HttpResponse, redirect
from .models import News, SportNews, RegistrationData
from .forms import RegistrationForm

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


def Register(request):
    context = {
        "form": RegistrationForm
    }
    return render(request, 'singup.html', context)


def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password'],
                                      email=form.cleaned_data['email'],
                                      phone=form.cleaned_data['phone']
                                      )
        myregister.save()

    return redirect('home')
