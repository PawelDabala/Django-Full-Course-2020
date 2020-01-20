

from django.urls import path
from .views import News, Contact, Home

urlpatterns = [
    path('', Home, name='home'),
    path('news/', News, name='news'),
    path('contact/', Contact, name='contact')
]
