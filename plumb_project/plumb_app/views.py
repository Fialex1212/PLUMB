from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import CreateUserForm, CreateCommentForm
from django.contrib import messages
from .models import Movie, Series, Anime, News, Comment, UserSavedMovie
import random


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


def news_page(requset):
    news = News.objects.all
    context = {'news': news}
    return render(requset, 'plumb_app/news.html', context)


def support(request):
    return render(request, 'plumb_app/support.html')


def cinemas(request):
    return render(request, 'plumb_app/cinemas.html')


def search(request):
    movies = Movie.objects.all()
    query = request.GET.get('query')
    if query:
        movies = Movie.objects.filter(title__icontains=query)

    context = {'movies': movies, "query": query}
    return render(request, 'plumb_app/search.html', context)


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


@login_required(login_url='login')
def user_page(request, pk):
    user = User.objects.get(pk=pk)
    context = {'user': user}
    return render(request, 'plumb_app/user/user.html', context)


@login_required(login_url='login')
def user_favorite(requset, pk):
    user = User.objects.get(pk=pk)
    context = {'user': user}
    return render(requset, 'plumb_app/user/user_saved.html', context)


@login_required(login_url='login')
def you(request):
    user = request.user
    if request.user.pk == user.pk:
        context = {'user': user, 'title': you}
        return render(request, 'plumb_app/user/you.html', context)
    else:
        redirect('home')


@login_required(login_url='login')
def you_saved(request):
    saved_movies = UserSavedMovie.objects.filter(user=request.user)
    user = request.user
    if request.user.pk == user.pk:
        context = {'user': user, 'saved_movies': saved_movies}
        return render(request, 'plumb_app/user/you_saved.html', context)
    else:
        return redirect('home')


@login_required(login_url='login')
def you_change_username(request):
    user = request.user
    if request.user.pk == user.pk:
        if request.method == "POST":
            newusername = request.POST.get('newusername')
            if User.objects.filter(username=newusername).exists():
                messages.error(request, "Username already taken")
            else:
                user.username = newusername
                user.save()

                logout(request)

                messages.success(request, "Username successfully changed. Please log in again")

                return redirect('login')

        context = {'user': user}
        return render(request, 'plumb_app/user/change_username.html', context)
    else:
        return redirect('home')


@login_required(login_url='login')
def you_change_password(request):
    user = request.user
    if request.user.pk == user.pk:
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            logout(request)
            messages.success(request, "Password was successfully changed!")
            return  redirect('login')
        else:
            messages.error(request, 'Password is incorrect')
        context = {'user': user, 'form': form}
        return render(request, 'plumb_app/user/change_password.html', context)
    else:
        return redirect('home')


@login_required(login_url='login')
def you_change_email(request):
    user = request.user
    if request.user.pk == user.pk:
        if request.method == "POST":
            new_email = request.POST.get('newuseremail')
            if User.objects.filter(email=new_email).exists():
                messages.error(request, "Email already taken")
            else:
                user.email = new_email
                user.save()

                logout(request)

                messages.success(request, "User email successfully changed. Please log in again")

                return redirect('login')

        context = {'user': user}
        return render(request, 'plumb_app/user/change_email.html', context)
    else:
        return redirect('home')


@login_required(login_url='login')
def you_delete_account(request):
    user = request.user
    if request.user.pk == user.pk:
        if request.method == "POST":
            checkpassword = request.POST.get('checkpassword')
            if user.password == checkpassword:
                user.delete()
                logout(request)
                messages.success(request, "User account successfully deleted.")
                return redirect('login')
        context = {'user': user}
        return render(request, 'plumb_app/user/delete_account.html', context)
    else:
        return redirect('home')


def logout_page(request):
    logout(request)
    return redirect('login')


#movie

def movie(request):
    return render(request, 'plumb_app/movie/movie.html')


def exactly_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    comments = Comment.objects.filter(movie=movie)
    user_saved_movie = UserSavedMovie.objects.filter(user=request.user, movie=movie).first()
    form = CreateCommentForm()
    if request.method == "POST":
        form = CreateCommentForm()
        if form.is_valid():
            form.instance.user = request.user
            form.save()
    context = {'movie' : movie, 'comments': comments, 'form': form,  'user_saved_movie': user_saved_movie}
    print(Movie.objects.count(), "total number of movies")
    return render(request, 'plumb_app/movie/exactly_movie.html', context)


def random_movie(request):
    total_movies = Movie.objects.count()
    random_pk = random.randint(1, total_movies)
    return redirect('exactly_movie', pk=random_pk)


def save_movie(request, movie_id):
    movie = Movie.objects.all(id=movie_id)
    user = request.user
    saved_movie = UserSavedMovie.objects.get_or_create(user=user,  movie=movie)
    saved_movie.is_liked = True
    saved_movie.save()
    return redirect('exactly_movie', pk=movie_id)

#series

def series_page(request):
    return render(request, 'plumb_app/series/series.html')


def current_series(request, pk):
    series = Series.objects.get(pk=pk)
    context = {'series' : series}
    return render(request, 'plumb_app/series/exactly_movie.html', context)


#anime

def anime(request):
    return render(request, 'plumb_app/anime/anime.html')


def current_anime(request, pk):
    return render(request, 'plumb_app/anime/current_anime.html')


#errors

def error_404(request):
    return render(request, 'plumb_app/errors/error_404.html')


def error_500(request):
    return render(request, 'plumb_app/errors/error_500.html')