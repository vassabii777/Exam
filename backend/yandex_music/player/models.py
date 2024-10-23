from turtle import title
from django.db              import models
from authentication_.models import User
from uuid                   import uuid4



class Artist(models.Model):
    id    =   models.UUIDField(default=uuid4, primary_key=True)
    name  =   models.CharField(max_length=255)
    bio   =   models.TextField(blank=True, null=True)
    image =   models.ImageField(upload_to='artists/', blank=True, null=True)

    spotify_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    
# Модель альбомов
class Album(models.Model):
    id     = models.UUIDField(default=uuid4, primary_key=True)
    title  = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')

    release_date = models.DateField()
    spotify_id   = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist.name}"
    
# Модель Трэков
class Track(models.Model):
    id     = models.UUIDField(default=uuid4, primary_key=True)
    title  = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='tracks')
    album  = models.ForeignKey(Album,  on_delete=models.CASCADE, related_name='tracks', blank=True, null=True)

    audio_file   = models.FileField(upload_to='tracks')
    duration     = models.DurationField()
    release_date = models.DateField(null=True, blank=True)
    preview_url  = models.URLField(blank=True, null=True)

    spotify_id   = models.CharField(max_length=255, blank=True, null=True)

    

    def __str__(self):
        return f"{self.title} by {self.artist.name}"

# модель Плэйлистов 
class Playlist(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists', null=True, blank=True)
    tracks = models.ManyToManyField(Track, related_name='playlists')
    created_at = models.DateTimeField(auto_now_add=True)
    
    release_date = models.DateField(null=True, blank=True)
    spotify_id   = models.CharField(max_length=255, blank=True, null=True)

    
    def __str__(self):
        return  f"{self.name} by {self.user.username}"