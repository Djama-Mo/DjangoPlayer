from django.urls import path
from .views import *

urlpatterns = [
    path('', SongView.as_view(), name='Home'),
    path('genre/<int:genre_id>/', GenreView.as_view(), name='Genre'),
    path('release/', ReleaseView.as_view(), name='Release'),
]
