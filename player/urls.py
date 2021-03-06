from django.urls import path
from .views import *


app_name = 'player'
urlpatterns = [
    path('', SongView.as_view(), name='Home'),
    path('genre/<int:genre_id>/', GenreView.as_view(), name='Genre'),
    path('release/', ReleaseView.as_view(), name='Release'),
    path('favourite/', ReleaseView.as_view(), name='Favourite'),
    path('add-favourite/<int:song_id>/', add_favourite_song, name='AddFavourite'),

    path('top-30/', top_songs, name='Top'),
    # path('delete-favourite/<int:song_id>/', delete_favourite_song, name='DeleteFavourite'),
]
