from django.shortcuts import render

from .models import Song, Genre
from .forms import SongForm

# Create your views here.
def index(request):
    songs = Song.objects.all()
    context = {'title': 'Home Page',
               'objects': songs}
    return render(request, 'player/index.html', context=context)


def get_genre(request, genre_id):
    songs = Song.objects.filter(genre_id=genre_id)
    genre = Genre.objects.get(id=genre_id).title
    context = {'title': genre,
               'objects': songs}
    return render(request, 'player/genre.html', context=context)


def release(request):
    if request.method == 'POST':
        pass
    else:
        form = SongForm()
    context = {'form': form}
    return render(request, 'player/release.html', context=context)
