from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('movies/', views.movies_index, name='index'),
    path('movies/<int:movie_id>/', views.movie_detail, name='detail'),
    path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movies_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movies_delete'),
    path('movies/<int:movie_id>/add_view/', views.add_view, name='add_view'),
    path('streams/', views.StreamList.as_view(), name='streams_index'),
    path('streams/<int:pk>/', views.StreamDetail.as_view(), name='streams_detail'),
    path('streams/create/', views.StreamCreate.as_view(), name='streams_create'),
    path('streams/<int:pk>/update/', views.StreamUpdate.as_view(), name='streams_update'),
    path('streams/<int:pk>/delete/', views.StreamDelete.as_view(), name='streams_delete'),
]