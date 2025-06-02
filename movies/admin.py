from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'genre', 'director')
    search_fields = ('title', 'director', 'genre')
    list_filter = ('genre', 'year')