

from django.urls import path
from .views import NewsP, Contact, Home

urlpatterns = [
    path('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path('contact/', Contact, name='contact')
]
