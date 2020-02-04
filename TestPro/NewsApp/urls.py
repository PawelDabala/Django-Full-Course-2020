

from django.urls import path
from .views import NewsP, Contact, Home, NewsDate, Register, addUser, modelform, addModalForm, Home2

urlpatterns = [
    path('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path('contact/', Contact, name='contact'),
    path('newsdate/<int:year>', NewsDate, name='newsdate'),
    path('singup/', Register, name='register'),
    path('addUser', addUser, name='addUser'),
    path('modalform/', modelform, name='form'),
    path('addmodalform/', addModalForm, name='modalform'),
    path('home2/', Home2, name='home2')

]
