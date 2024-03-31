from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages
from .models import Movie, Series, Anime


#login/sing up

def sing_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)

            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if form.is_valid():
                user = form.save(commit=False)
                user.username = username
                user.email = email
                user.set_password(password1)
                user.save()
                messages.success(request, "Account was created" + username)
                return redirect('login')
            else:
                pass
    context = {form: 'form'}
    return render(request, 'plumb_app/login_singup/sing_up.html', context)



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password incorrect')

    return render(request, 'plumb_app/login_singup/login.html')


#main

def preloader(requset):
    return render(requset, 'plumb_app/preloader.html')


def home(request):
    return render(request, 'plumb_app/home.html')


def news(requset):
    return render(requset, 'plumb_app/news.html')


def support(request):
    return render(request, 'plumb_app/support.html')


def cinemas(request):
    return render(request, 'plumb_app/cinemas.html')


#watch


def watch(requset):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(requset, 'plumb_app/watch/watch.html', context)


def watch_recommends(requset):
    return render(requset, 'plumb_app/watch/recommends.html')


def watch_byrating(requset):
    return render(requset, 'plumb_app/watch/by_rating.html')


def watch_announcement(request):
    return render(request, 'plumb_app/watch/announcement.html')


def watch_bygenre(request):
    return render(request, 'plumb_app/watch/by_gener.html')


#user


def user_page(request, pk):
    user = User.objects.get(pk=pk)
    context = {'user': user}
    return render(request, 'plumb_app/user/user.html', context)


def user_favorite(requset, pk):
    user = User.objects.get(pk=pk)
    context = {'user': user}
    return render(requset, 'plumb_app/user/user_favorite.html', context)


#movie

def movie(request):
    return render(request, 'plumb_app/movie/movie.html')


def current_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    context = {'movie' : movie}
    return render(request, 'plumb_app/movie/current_movie.html', context)


#series

def series_page(request):
    return render(request, 'plumb_app/series/series.html')


def current_series(request, pk):
    series = Series.objects.get(pk=pk)
    context = {'series' : series}
    return render(request, 'plumb_app/series/current_series.html', context)


#anime

def anime(request):
    return render(request, 'plumb_app/anime/anime.html')


def current_anime(request, pk):
    return render(request, 'plumb_app/anime/current_anime.html')