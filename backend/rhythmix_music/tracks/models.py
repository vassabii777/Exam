from django.db      import models
from uuid           import uuid4
from artists.models import Artist
from albums.models  import Album



# Модель Трэков
class Track(models.Model):
    id     = models.UUIDField(default=uuid4, primary_key=True)
    title  = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='tracks')
    album  = models.ForeignKey(Album,  on_delete=models.CASCADE, related_name='tracks', blank=True, null=True)

    file = models.FileField(upload_to='tracks/', null=True, blank=True) 
    duration     = models.DurationField()
    release_date = models.DateField(null=True, blank=True)
    preview_url  = models.URLField(blank=True, null=True)

    spotify_id   = models.CharField(max_length=255, blank=True, null=True)

    

    def __str__(self):
        return f"{self.title} by {self.artist.name}"
