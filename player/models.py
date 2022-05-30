from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .duration_def import get_audio_length


class Song(models.Model):
    title = models.TextField('Title')
    artist = models.TextField('Artist')
    genre = models.ForeignKey('Genre', null=True, on_delete=models.SET_NULL)
    image = models.ImageField('Cover', default='song_default.png', upload_to='song_pic')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField('Audio')
    audio_link = models.CharField(max_length=256, blank=True, null=True)
    duration = models.CharField('Duration', max_length=64, default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.duration or self.duration == 0:
            # logic for getting length of audio
            audio_length = get_audio_length(self.audio_file)
            print(audio_length)
            self.duration = f'{audio_length:.2f}'

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'
        ordering = ['-id']


class Genre(models.Model):
    title = models.CharField('Genre', max_length=128, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Genre', kwargs={'genre_id': self.pk})

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
