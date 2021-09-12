from django import template

from users.models import Profile

register = template.Library()


@register.simple_tag()
def get_favourite_songs(**kwargs):
    user_pk = kwargs['user_pk']
    profile = Profile.objects.filter(user__pk=user_pk)[0]
    return profile.favourite_songs.all()
