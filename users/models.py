from django.db import models
from django.contrib.auth.models import User
from player.models import Song


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='user_pic', default='user_default')
    favourite_songs = models.ManyToManyField(Song, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'
