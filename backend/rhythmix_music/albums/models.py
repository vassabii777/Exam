from django.db import models
from uuid import uuid4
from artists.models import Artist

# Модель альбомов
class Album(models.Model):
    id     = models.UUIDField(default=uuid4, primary_key=True)
    title  = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')

    release_date = models.DateField()   
    spotify_id   = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist.name}"