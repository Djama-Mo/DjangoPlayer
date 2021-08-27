from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Song, Genre
from .forms import SongForm


class SongView(ListView):
    model = Song
    template_name = 'player/index.html'
    extra_context = {'title': 'Home Page'}
    context_object_name = 'objects'


# def index(request):
#     songs = Song.objects.all()
#     context = {'title': 'Home Page',
#                'objects': songs}
#     return render(request, 'player/index.html', context=context)
#
#
def get_genre(request, genre_id):
    songs = Song.objects.filter(genre_id=genre_id)
    genre = Genre.objects.get(id=genre_id).title
    context = {'title': genre,
               'objects': songs}
    return render(request, 'player/genre.html', context=context)


def release(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect(song)
    else:
        form = SongForm()
    context = {'form': form}
    return render(request, 'player/release.html', context=context)
