from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Song, Genre
from .forms import SongForm


class SongView(ListView):
    model = Song
    template_name = 'player/index.html'
    context_object_name = 'objects'
    queryset = Song.objects.select_related('genre')
    paginate_by = 1
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'
        return context


class GenreView(SongView):
    template_name = 'player/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Genre.objects.get(pk=self.kwargs['genre_id']).title
        return context

    def get_queryset(self):
        return Song.objects.filter(genre_id=self.kwargs['genre_id']).select_related('genre')



class ReleaseView(LoginRequiredMixin, CreateView):
    template_name = 'player/release.html'
    form_class = SongForm
    login_url = '/admin'
    success_url = reverse_lazy('Home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context
