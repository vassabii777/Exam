from django.db import models
from uuid import uuid4

class Artist(models.Model):
    id    =   models.UUIDField(default=uuid4, primary_key=True)
    name  =   models.CharField(max_length=255)
    bio   =   models.TextField(blank=True, null=True)
    image =   models.ImageField(upload_to='artists/', blank=True, null=True)

    spotify_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    