from django.db import models
from django.utils import timezone
# Create your models here.


class News(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()
    pub_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.author


class SportNews(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.author


class RegistrationData(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Article3(models.Model):
    """Model definition for Aritcle3."""

    # TODO: Define fields here
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        """Unicode representation of Aritcle3."""
        return self.title

