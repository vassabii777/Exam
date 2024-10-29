from django.db     import models
from django.conf   import settings
from uuid          import uuid4

from tracks.models import Track


# модель Плэйлистов 
class Playlist(models.Model):
    id         = models.UUIDField(default=uuid4, primary_key=True)
    name       = models.CharField(max_length=255)
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tracks     = models.ManyToManyField(Track, related_name='playlists')
    created_at = models.DateTimeField(auto_now_add=True)
    
    release_date = models.DateField(null=True, blank=True)
    spotify_id   = models.CharField(max_length=255, blank=True, null=True)

    
    def __str__(self):
        return  f"{self.name} by {self.user.username}"