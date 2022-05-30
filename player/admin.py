from django.contrib import admin
from .models import Song, Genre


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'genre', 'user')
    search_fields = ('title', 'artist', 'genre')
    list_display_links = ('title', )
    list_filter = ('genre', )


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title', )


admin.site.register(Song, SongAdmin)
admin.site.register(Genre, GenreAdmin)
