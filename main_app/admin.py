from django.contrib import admin
from .models import Movie, View, Stream

admin.site.register(Movie)
admin.site.register(View)
admin.site.register(Stream)