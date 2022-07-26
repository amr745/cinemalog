from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Movie, Stream
from .forms import ViewForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'cinemalog-ar-83'

class MovieCreate(LoginRequiredMixin, CreateView):
  model = Movie
  fields = ['title', 'synopsis', 'date', 'rating', 'genre', 'url']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class MovieUpdate(LoginRequiredMixin, UpdateView):
  model = Movie
  fields = ['synopsis', 'date', 'rating', 'genre', 'url']

class MovieDelete(LoginRequiredMixin, DeleteView):
  model = Movie
  success_url = '/movies/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def movies_index(request):
  movies = Movie.objects.filter(user=request.user)
  return render(request, 'movies/index.html', { 'movies': movies })

@login_required
def movie_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  streams_movie_doesnt_have = Stream.objects.exclude(id__in = movie.streams.all().values_list('id'))
  view_form = ViewForm()
  return render(request, 'movies/detail.html', {
    'movie': movie, 'view_form': view_form,
    'streams': streams_movie_doesnt_have
  })

@login_required
def add_view(request, movie_id):
  form = ViewForm(request.POST)
  if form.is_valid():
    new_view = form.save(commit=False)
    new_view.movie_id = movie_id
    new_view.save()
  return redirect('detail', movie_id=movie_id)

# @login_required
# def add_photo(request, movie_id):
#     photo_file = request.FILES.get('photo-file', None)
#     if photo_file:
#         s3 = boto3.client('s3')
#         key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
#         try:
#             s3.upload_fileobj(photo_file, BUCKET, key)
#             url = f"{S3_BASE_URL}{BUCKET}/{key}"
#             photo = Movie(url=url, movie_id=movie_id)
#             photo.save()
#         except:
#             print('An error occurred uploading file to S3')
#     return redirect('detail', movie_id=movie_id)

class StreamList(LoginRequiredMixin, ListView):
  model = Stream

class StreamDetail(LoginRequiredMixin, DetailView):
  model = Stream

class StreamCreate(LoginRequiredMixin, CreateView):
  model = Stream
  fields = '__all__'

class StreamUpdate(LoginRequiredMixin, UpdateView):
  model = Stream
  fields = ['name', 'color']

class StreamDelete(LoginRequiredMixin, DeleteView):
  model = Stream
  success_url = '/stream/'

@login_required
def assoc_stream(request, movie_id, stream_id):
  Movie.objects.get(id=movie_id).streams.add(stream_id)
  return redirect('detail', movie_id=movie_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
