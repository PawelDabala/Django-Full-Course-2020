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

    def ShortenText(self):
        return self.body[:5]


class ContactInfo(models.Model):
    """Model definition for ContactInfo."""

    # TODO: Define fields here
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    address = models.CharField(max_length=30)

    class Meta:
        abstract = True


class Customer(ContactInfo):
    """Model definition for Customer."""

    # TODO: Define fields here
    phone = models.CharField(max_length=30)


class Staf(ContactInfo):
    """Model definition for Staf."""

    # TODO: Define fields here
    position = models.CharField(max_length=30)


class Place(models.Model):
    """Model definition for Place."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        """Unicode representation of Place."""
        return self.name


class Restaurant(Place):
    """Model definition for Restaurant."""

    # TODO: Define fields here
    servers_pizza = models.BooleanField(default=False)
    serves_tuna = models.BooleanField(default=False)

