
from django.shortcuts import render, HttpResponse, redirect
from .models import News, SportNews, RegistrationData, Article3
from .forms import RegistrationForm, RegistrationDataModel
from django.contrib import messages


# Create your views here.


def Home(request):

    article = Article3.objects.all()
    context = {
       "articles": article
    }
    return render(request, 'index.html', context)


def Home2(request):

    article = Article3.objects.all()
    context = {
       "articles":article
    }
    return render(request, 'home.html', context)


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
        messages.add_message(request, messages.SUCCESS,
                             'You have singup successfuly ')

    return redirect('register')


def modelform(request):

    context = {
        'modalform': RegistrationDataModel
    }
    return render(request, 'modelform.html', context)


def addModalForm(request):
    mymodalform = RegistrationDataModel(request.POST)

    if mymodalform.is_valid():
        mymodalform.save()

    return redirect('form')


    
