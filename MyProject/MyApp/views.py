from django.shortcuts import render, req

# Create your views here.


def Home(request):

    

    context = {

    }

    return render(request, 'home.html', context)
