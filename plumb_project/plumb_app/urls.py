from django.urls import path
from .views import *


urlpatterns = [
    #login/sign up
    path('login/', loginPage, name='login'),
    path('sing-up/', sing_up, name='sing_up'),

    #profile
    path('user/<int:pk>/', user_page, name='user'),
    path('user/<int:pk>/favorite', user_favorite, name='favorite'),

    #main
    path('load/', preloader, name='preloader'),
    path('home/', home, name='home'),
    path('news/', news, name='news'),
    path('support/', support, name='support'),
    path('cinemas/', cinemas, name='cinemas'),

    #watch
    path('watch/', watch, name='watch'),
    path('watch/recommends/', watch_recommends, name='recommends'),
    path('watch/by-rating/',  watch_byrating, name='by_rating'),
    path('watch/announcement/', watch_announcement, name='announcement'),
    path('watch/by-genre/', watch_bygenre, name='by_gener'),

    #movie
    path('movie', movie),
    path('movie/<int:id>/',  current_movie),

    #series
    path('series/', series_page),
    path('series/<int:id>/', current_series),

    #anime
    path('anime/', anime),
    path('anime/<int:id>', current_anime),
]