from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Movie, Stream
from .forms import ViewForm

class MovieCreate(CreateView):
  model = Movie
  fields = '__all__'

class MovieUpdate(UpdateView):
  model = Movie
  fields = ['synopsis', 'date', 'rating', 'genre', 'url']

class MovieDelete(DeleteView):
  model = Movie
  success_url = '/movies/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', { 'movies': movies })

def movie_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  view_form = ViewForm()
  return render(request, 'movies/detail.html', {
    'movie': movie, 'view_form': view_form
  })

def add_view(request, movie_id):
  form = ViewForm(request.POST)
  if form.is_valid():
    new_view = form.save(commit=False)
    new_view.movie_id = movie_id
    new_view.save()
  return redirect('detail', movie_id=movie_id)

class StreamList(ListView):
  model = Stream

class StreamDetail(DetailView):
  model = Stream

class StreamCreate(CreateView):
  model = Stream
  fields = '__all__'

class StreamUpdate(UpdateView):
  model = Stream
  fields = ['name', 'color']

class StreamDelete(DeleteView):
  model = Stream
  success_url = '/stream/'