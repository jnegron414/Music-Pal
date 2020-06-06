from django.db import models
from django.db.models import Q


class Artist(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    website = models.URLField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.question_text

    def all_songs(self):
        from music.models import Song
        return Song.objects.filter(Q(artist=self) | Q(featured_artists__in=[self]))

    def songs(self):
        from music.models import Song
        return Song.objects.filter(artist=self)

    def featured_songs(self):
        from music.models import Song
        return Song.objects.filter(featured_artists__in=[self])

    def albums(self):
        from music.models import Album
        return Album.objects.filter(artist=self)
