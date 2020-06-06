from django.db import models

from artists.models import Artist


class Album(models.Model):
    title = models.CharField(max_length=150)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_art = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.question_text

    def songs(self):
        return Song.objects.filter(album=self)


class Song(models.Model):
    title = models.CharField(max_length=150)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    length = models.TimeField()
    featured_artists = models.ManyToManyField(Artist, blank=True, related_name='featured_artists')


