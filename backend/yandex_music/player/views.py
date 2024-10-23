from rest_framework import generics
from .serializers import TrackSerializer, AlbumSerializer, ArtistSerializer, PlaylistSerializer, PlaylistImportSerializer
from .models import Track, Album, Artist, Playlist
from rest_framework.permissions import IsAuthenticated


from rest_framework import status


from rest_framework.response import Response
from rest_framework.views import APIView
from .services import(
     import_artist_from_spotify,
     import_track_from_spotify,
     import_playlist_from_spotify,
     import_album_from_spotify,
     
)


#ARTIST VIEWS
class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer



class ArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


#ALBUM VIEWS 
class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


# Track views
class TrackListCreateView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class TrackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

# Playlist views
class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer



class SpotifyImportArtistView(APIView):
    def post(self, request):
        artist_name = request.data.get('artist_name')
        
        if not artist_name:
            return Response({"errors": "Artist name is required"}, status=400)
        
        result = import_artist_from_spotify(artist_name)
        
        if "successfully" in result.lower():
            return Response({"message": result}, status=200)
        else:
            return Response({"errors": result}, status=400)
    

class SpotifyImportTrackView(APIView):
    def post(self, request):
        track_name = request.data.get('track_name')

        if not track_name:
            return Response({"error": "Track name is required"} ,status=400)
        
        result = import_track_from_spotify(track_name)
        
        if "successfully" in result.lower():
            return Response({"message": result}, status=200)
        else:


            return Response({"errors": result}, status=400)
        

class ImportPlaylistView(APIView):
    def post(self, request):
        serializer = PlaylistImportSerializer(data=request.data)
        if serializer.is_valid():
            playlist_name = serializer.validated_data['playlist_name']
            result = import_playlist_from_spotify(playlist_name)
            
            if result:
                return Response({'message': result}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Import failed'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SpotifyImportAlbumView(APIView):
    def post(self, request):
        album_name = request.data.get('album_name')

        if not album_name:
            return Response({"error": "Album name is required"})
        
        result = import_album_from_spotify(album_name)

        if "successfully":
            return Response({"message": result}, status=200)
        else:
            return Response({"errors": result}, status=400)