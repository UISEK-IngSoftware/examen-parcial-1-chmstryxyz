from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título de la película")
    genre = models.CharField(max_length=100, verbose_name="Género")
    director = models.CharField(max_length=100, verbose_name="Director")
    year = models.PositiveIntegerField(verbose_name="Año de publicación")
    synopsis = models.TextField(verbose_name="Sinopsis")

    def __str__(self):
        return f"{self.title} ({self.year})"