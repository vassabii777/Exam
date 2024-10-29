from rest_framework   import generics
from .models          import Track
from .serializers     import TrackSerializer
from services.services import import_track_from_spotify
from rest_framework   import response


from rest_framework.response    import Response
from rest_framework.permissions import IsAuthenticated
from playlists.serializers      import PlaylistSerializer
from rest_framework.views       import APIView
from django.core.cache          import cache



class TrackListCreateView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    def get_queryset(self):
        # Получаем параметр поиска
        track_name = self.request.query_params.get('search')

        # Если параметр поиска присутствует, ищем в кеше
        if track_name:
            cache_key = f"track_search_{track_name}"
            cached_tracks = cache.get(cache_key)

            if cached_tracks:
                # Если треки найдены в кеше, возвращаем их
                return cached_tracks
            
            # Если трек не найден в кеше, ищем в базе данных
            tracks = Track.objects.filter(title__icontains=track_name)
            if tracks.exists():
                # Сохраняем результаты в кеше на 1 час
                cache.set(cache_key, tracks, timeout=3600)
                return tracks
            else:
                # Если трек не найден, импортируем его из Spotify и кешируем результат
                result = import_track_from_spotify(track_name)
                if "successfully" in result.lower():
                    # Обновляем кеш с новым треком
                    new_tracks = Track.objects.filter(title__icontains=track_name)
                    cache.set(cache_key, new_tracks, timeout=864000)
                    return new_tracks
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

            # Обновляем кеш
            cache_key = f"playlist_{playlist.id}_tracks"
            cache.delete(cache_key)  # Очистка кеша после обновления

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
        


