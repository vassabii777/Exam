from rest_framework import generics
from .models import Playlist
from .serializers import PlaylistSerializer, PlaylistCreateSerializer, PlaylistImportSerializer
from rest_framework.permissions import IsAuthenticated

from services import import_playlist_from_spotify
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

# Playlist views
class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Если запрос содержит параметр поиска, ищем плейлист по названию
        playlist_name = self.request.query_params.get('search')
        if playlist_name:
            # Пытаемся найти плейлист в базе данных
            playlists = Playlist.objects.filter(name__icontains=playlist_name, user=self.request.user)
            if playlists.exists():
                return playlists
            else:
                # Если плейлист не найден, импортируем его из Spotify
                result = import_playlist_from_spotify(playlist_name)
                if "successfully" in result.lower():
                    # Обновляем queryset с новым плейлистом
                    return Playlist.objects.filter(name__icontains=playlist_name, user=self.request.user)
        # Если нет параметра поиска, возвращаем плейлисты пользователя
        return Playlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Создаем плейлист и привязываем его к пользователю
        serializer.save(user=self.request.user)



class PlaylistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer






class UserPlaylistCreateView(generics.CreateAPIView):
    serializer_class = PlaylistCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserPlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)
    

class SpotifyImportPlaylistView(APIView):
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

