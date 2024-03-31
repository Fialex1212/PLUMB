from django.db import models


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=192)
    img = models.ImageField()
    description = models.TextField()
    year = models.IntegerField()
    genre = models.CharField(max_length=120)
    director = models.CharField(max_length=120)
    comments = models.ManyToManyField(Comment, related_name='movie_comments')


class Series(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=192)
    img = models.ImageField()
    description = models.TextField()
    year = models.IntegerField()
    genre = models.CharField(max_length=120)
    director = models.CharField(max_length=120)
    comments = models.ManyToManyField(Comment, related_name='series_comments')


class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=192)
    img = models.ImageField()
    description = models.TextField()
    year = models.IntegerField()
    genre = models.CharField(max_length=120)
    director = models.CharField(max_length=120)
    comments = models.ManyToManyField(Comment, related_name='anime_comments')


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)


