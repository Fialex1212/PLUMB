from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=192)
    img = models.ImageField()
    description = models.TextField()
    year = models.IntegerField()
    genre = models.CharField(max_length=120)
    director = models.CharField(max_length=120)


class Series(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=192)
    img = models.ImageField()
    description = models.TextField()
    year = models.IntegerField()
    genre = models.CharField(max_length=120)
    director = models.CharField(max_length=120)


class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=192)
    img = models.ImageField()
    description = models.TextField()
    year = models.IntegerField()
    genre = models.CharField(max_length=120)
    director = models.CharField(max_length=120)


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class UserSavedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True, null=False)


