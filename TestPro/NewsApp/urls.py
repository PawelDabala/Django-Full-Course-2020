

from django.urls import path
from .views import NewsP, Contact, Home, NewsDate, Register, addUser

urlpatterns = [
    path('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path('contact/', Contact, name='contact'),
    path('newsdate/<int:year>', NewsDate, name='newsdate'),
    path('singup/', Register, name='register'),
    path('addUser', addUser, name='addUser')
]
