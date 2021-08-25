from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    title = models.TextField('Title')
    artist = models.TextField('Artist')
    genre = models.ForeignKey('Genre', null=True, on_delete=models.SET_NULL)
    image = models.ImageField('Image', default='song_default.png', upload_to='song_pic')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(blank=True, null=True)
    audio_link = models.CharField(max_length=256, blank=True, null=True)
    duration = models.CharField('Duration', max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'


class Genre(models.Model):
    title = models.CharField('Genre', max_length=128, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
