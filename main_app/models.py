from django.db import models
from datetime import date
from django.urls import reverse

GENRE = (
    ('D', 'Drama'),
    ('T', 'Thriller'),
    ('R', 'Romance'),
    ('A', 'Action'),
    ('C', 'Comedy'),
    ('H', 'Horror'),
    ('S', 'Science Fiction'),
    ('F', 'Fantacy'),
)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField(max_length=250)
    date = models.DateField('release date')
    rating = models.CharField(max_length=10)
    genre = models.CharField(
    max_length=1,
        choices=GENRE,
        default=GENRE[0][0]
    )
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})