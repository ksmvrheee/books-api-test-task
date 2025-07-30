from django.db import models


class Book(models.Model):
    """Represents a book having a title, an author and a year of publishing."""
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_year = models.PositiveIntegerField()
