from django.db     import models

from django.conf   import settings

from tracks.models import Track


class UserTrackInteraction(models.Model):
    user      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    track     = models.ForeignKey(Track,on_delete=models.CASCADE)
    rating    = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)