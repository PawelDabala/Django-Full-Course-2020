from django.contrib import admin
from .models import Publication, Article, Article2, Reporter, Place, Restaurant

# Register your models here.
admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(Article2)
admin.site.register(Reporter)
admin.site.register(Place)
admin.site.register(Restaurant)
