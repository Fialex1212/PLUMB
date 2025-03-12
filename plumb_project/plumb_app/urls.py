from django.urls import path
from .views import *


urlpatterns = [
    #login/sign up
    path('login/', loginPage, name='login'),
    path('sing-up/', sing_up, name='sing_up'),

    #user
    path('you/', you, name='you'),
    path('you/saved/', you_saved, name='you_saved'),
    path('you/change-username/', you_change_username, name='change_username'),
    path('you/change-email/', you_change_email, name='change_email'),
    path('you/change-password/', you_change_password, name='change_password'),
    path('you/delete-account/', you_delete_account, name='delete_account'),
    path('user/<int:pk>/', user_page, name='user'),
    path('user/<int:pk>/favorite', user_favorite, name='user_saved'),
    path('you/logout/', logout_page, name='logout_page'),

    #main
    path('', preloader, name='preloader'),
    path('home/', home, name='home'),
    path('news/', news_page, name='news'),
    path('support/', support, name='support'),
    path('cinemas/', cinemas, name='cinemas'),
    path('search/', search, name='search'),
    path('search/<str:query>/', search, name='search_with_query'),

    #watch
    path('watch/', watch, name='watch'),
    path('watch/recommends/', watch_recommends, name='recommends'),
    path('watch/by-rating/',  watch_byrating, name='by_rating'),
    path('watch/announcement/', watch_announcement, name='announcement'),
    path('watch/by-genre/', watch_bygenre, name='by_gener'),

    #movie
    path('movie', movie),
    path('movie/<int:pk>/',  exactly_movie, name='exactly_movie'),
    path('random-movie/', random_movie, name='random_movie'),

    #series
    path('series/', series_page),
    path('series/<int:id>/', current_series),

    #anime
    path('anime/', anime),
    path('anime/<int:id>', current_anime),
]