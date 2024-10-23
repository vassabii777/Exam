from rest_framework import serializers
from .models import Artist, Album, Track, Playlist



class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model  =Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only = True)

    class Meta:
        model  = Album
        fields = '__all__'
    

class TrackSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = Track
        fields = '__all__'


class PlaylistImportSerializer(serializers.Serializer):
    playlist_name = serializers.CharField(max_length=255)


class PlaylistSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    tracks = TrackSerializer(many=True, read_only=True)
    
    class Meta:
        model = Playlist
        fields = '__all__'
