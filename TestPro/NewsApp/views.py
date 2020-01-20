from django.shortcuts import render, HttpResponse


# Create your views here.

def News(request):
    return HttpResponse("<h1> This is our latest news<h1>")
    
