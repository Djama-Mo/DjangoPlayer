from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='user_pic', default='user_default')

    def __str__(self):
        return f'{self.user.username} Profile'
