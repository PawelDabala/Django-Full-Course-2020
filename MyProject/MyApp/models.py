from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Publication(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    title = models.CharField(max_length=30)

    class Meta:
        """Meta definition for MODELNAME."""

        # verbose_name = 'MODELNAME'
        # verbose_name_plural = 'MODELNAMEs'
        ordering = ('title',)

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.title


class Article(models.Model):
    """Model definition for Article."""

    # TODO: Define fields here
    headline = models.CharField(max_length=300)
    publications = models.ManyToManyField(Publication)

    class Meta:
        """Meta definition for Article."""
        ordering = ('headline',)

    def __str__(self):

        return self.headline


class Reporter(models.Model):
    """Model definition for Reporter."""

    # TODO: Define fields here
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Article2(models.Model):
    """Model definition for Article2."""

    # TODO: Define fields here
    headline = models.CharField(max_length=30)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    class Meta:
        ordering = ('headline',)

    def __str__(self):
        """Unicode representation of Article2."""
        return self.headline


class Place(models.Model):
    """Model definition for Place
."""
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __str__(self):
        """Unicode representation of Place
    ."""
        return self.name


class Restaurant(models.Model):
    """Model definition for Restaurant."""

    # TODO: Define fields here
    place = models.OneToOneField(
        Place, on_delete=models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves = models.BooleanField(default=False)

    def __str__(self):
        """Unicode representation of Restaurant."""
        return self.place.name


class Article3(models.Model):
    """Model definition for Aritcle3."""

    # TODO: Define fields here
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        """Unicode representation of Aritcle3."""
        return self.title



class MyUser(User):
    """Model definition for MyUser."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for MyUser."""
        ordering = ('username',)
        proxy = True
        
            

   