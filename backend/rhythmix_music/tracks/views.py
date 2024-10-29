from rest_framework import generics
from .models        import Track
from .serializers   import TrackSerializer
from services       import import_track_from_spotify
from rest_framework import response
from rest_framework.permissions import IsAuthenticated
from playlists.serializers import PlaylistSerializer
from rest_framework.views import APIView

# TRACK VIEWs
class TrackListCreateView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    def get_queryset(self):
        # Если запрос содержит параметр поиска, ищем трек по названию
        track_name = self.request.query_params.get('search')
        if track_name:
            tracks = Track.objects.filter(title__icontains=track_name)
            if tracks.exists():
                return tracks
            else:
                # Если трек не найден, импортируем из Spotify
                result = import_track_from_spotify(track_name)
                if "successfully" in result.lower():
                    # Обновляем queryset с новым треком
                    return Track.objects.filter(title__icontains=track_name)
        return super().get_queryset()
    

class TrackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer



class SpotifyImportTrackView(APIView):
    def post(self, request):
        track_name = request.data.get('track_name')

        if not track_name:
            return response.Response({"error": "Track name is required"} ,status=400)
        
        result = import_track_from_spotify(track_name)
        
        if "successfully" in result.lower():
            return response.Response({"message": result}, status=200)
        else:


            return response.Response({"errors": result}, status=400)
        


class UserAddTrackPlaylistView(generics.UpdateAPIView):
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        playlist = self.get_object()
        track_id = request.data.get('track_id')
        try:
            track = Track.objects.get(id=track_id)
            playlist.tracks.add(track)
            return Response({'message': f'Track "{track.title}" added to playlist "{playlist.name}".'}, status=status.HTTP_200_OK)
        except Track.DoesNotExist:
            return Response({'error': 'Track not found'}, status=status.HTTP_404_NOT_FOUND)
    


class UserRemoveTrackFromPlaylistView(generics.UpdateAPIView):
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def update (self, request, *args, **kwargs):
        playlist = self.get_object()
        track_id = request.data.get('track_id')

        try:
            track = Track.objects.get(id=track)
            playlist.tracks.remove(track)
            return  Response({'message': f'Track "{track.title} removed from playlist "{playlist.name}".'}, status=status.HTTP_200_OK)
        except Track.DoesNotExist:
            return Response({'error': 'Track not found'}, status=status.HTTP_404_NOT_FOUND)
        