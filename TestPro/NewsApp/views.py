from django.shortcuts import render, HttpResponse


# Create your views here.
def Home(request):

    context = {
        "name": "Pawel",
        "number": 2332123
    }

    return render(request, 'index.html', context=context)


def News(request):
    context = {
        "list": ["Python", "Java", "C++", "C#", "Ruby"],
        "mynum": 40
    }
    return render(request, 'news.html', context=context)


def Contact(request):

    return render(request, 'contact.html')
