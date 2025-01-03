from django.db import models

# Create your models here.

class Book(models.Model):

    name = models.CharField(max_length=200)
    authors = models.JSONField()
    year_published = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name