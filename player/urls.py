from django.urls import path
from .views import *

urlpatterns = [
    path('', SongView.as_view(), name='Home'),
    path('genre/<int:genre_id>/', get_genre, name='Genre'),
    path('release/', release, name='Release'),
]
