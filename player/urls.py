from django.urls import path
from .views import *

urlpatterns = [
    path('', SongView.as_view(), name='Home'),
    path('genre/<int:genre_id>/', GenreView.as_view(), name='Genre'),
    path('release/', ReleaseView.as_view(), name='Release'),
    path('favourite/', ReleaseView.as_view(), name='Favourite'),
    path('add-favourite/<int:song_id>/', add_favourite_song, name='AddFavourite'),
    path('delete-favourite/<int:song_id>/', delete_favourite_song, name='DeleteFavourite'),
]
