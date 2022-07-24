from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Movie

# class Movie:
#   def __init__(self, title, date, description, rating, genre):
#     self.title = title
#     self.date = date
#     self.description = description
#     self.rating = rating
#     self.genre = genre

# movies = [
#   Movie('Thor: Love and Thunder', 'July 8, 2022', 'Thor enlists the help of Valkyrie, Korg and ex-girlfriend Jane Foster to fight Gorr the God Butcher, who intends to make the gods extinct.', 'PG-13', 'Action/Adventure/Comedy'),
#   Movie('Top Gun: Maverick', ' May 27, 2022', 'After more than thirty years of service as one of the Navy"s top aviators, Pete Mitchell is where he belongs, pushing the envelope as a courageous test pilot and dodging the advancemen','PG-13', 'Action/Drama'),
#   Movie('Nope', 'July 22, 2022', 'The residents of a lonely gulch in inland California bear witness to an uncanny and chilling discovery.', 'R', 'Horror/Mystery/Sci-Fi/Thriller'),
# ]

class MovieCreate(CreateView):
  model = Movie
  fields = '__all__'

class MovieUpdate(UpdateView):
  model = Movie
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['synopsis', 'date', 'rating', 'genre', 'url']

class MovieDelete(DeleteView):
  model = Movie
  success_url = '/movies/'

def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', { 'movies': movies })

def movie_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  return render(request, 'movies/detail.html', { 'movie': movie })