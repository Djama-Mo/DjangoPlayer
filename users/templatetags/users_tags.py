from django import template

from users.models import Profile

register = template.Library()


@register.simple_tag()
def get_favourite_songs(**kwargs):
    user_pk = kwargs['user_pk']
    profile = Profile.objects.filter(user__pk=user_pk)[0]
    return profile.favourite_songs.all().select_related('genre')


@register.simple_tag()
def get_like_status(**kwargs):
    user = kwargs['user']
    song = kwargs['song']
    songs = get_favourite_songs(user_pk=user.id)
    if song in songs:
        res = 'Unlike'
    else:
        res = 'Like'
    return res
