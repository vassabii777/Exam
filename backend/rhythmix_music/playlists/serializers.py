from .models import Playlist
from rest_framework import serializers

from tracks.serializers import TrackSerializer


class PlaylistImportSerializer(serializers.Serializer):
    playlist_name = serializers.CharField(max_length=255)


class PlaylistSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    tracks = TrackSerializer(many=True, read_only=True)
    
    class Meta:
        model = Playlist
        fields = '__all__'


class PlaylistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name']
