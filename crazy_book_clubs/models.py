from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    authors = models.JSONField()
    year_published = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.year_published})"

class Review(models.Model):
    my_review = models.TextField()
    stars = models.IntegerField()
    unfinished = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review for {self.book.name} - {self.stars} stars"
    
    class Meta:
        ordering = ['-date_added']

