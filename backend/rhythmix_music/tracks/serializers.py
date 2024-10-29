from rest_framework import serializers

from artists.serializers import ArtistSerializer
from albums.serializers import AlbumSerializer

from .models import Track


class TrackSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = Track
        fields = '__all__'