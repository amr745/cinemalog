from django.db import models
from django.urls import reverse
from datetime import date

RATINGS = (
    ('G', 'G'),
    ('P', 'PG'),
    ('T', 'PG-13'),
    ('R', 'R'),
    ('N', 'NC-17'),
)

GENRES = (
    ('D', 'Drama'),
    ('T', 'Thriller'),
    ('R', 'Romance'),
    ('A', 'Action'),
    ('C', 'Comedy'),
    ('H', 'Horror'),
    ('S', 'Science Fiction'),
    ('F', 'Fantacy'),
)

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening'),
)

class Stream(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('streams_detail', kwargs={'pk': self.id})

class Movie(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField(max_length=250)
    date = models.DateField('release date')
    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        default=RATINGS[2][0]
    )
    genre = models.CharField(
    max_length=1,
        choices=GENRES,
        default=GENRES[3][0]
    )
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})

class View(models.Model):
    date = models.DateField('view date')
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[2][0]
    )

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']