from django.shortcuts import render, HttpResponse


# Create your views here.
def Home(request):
    return HttpResponse("<h1>This is our home page<h1>")


def News(request):
    return HttpResponse("<h1> This is our latest news<h1>")


def Contact(request):
    return HttpResponse("<h1> This is contact us page <h1>")
