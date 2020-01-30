from django.db import models

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


