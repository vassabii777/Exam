from django.shortcuts import render
from rest_framework import generics
from .models import Album
from .serializers import AlbumSerializer

from services import import_album_from_spotify
from rest_framework.views import APIView

from rest_framework.response import Response

class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get_queryset(self):
        # Если запрос содержит параметр поиска, ищем альбом по названию
        album_name = self.request.query_params.get('search')
        if album_name:
            albums = Album.objects.filter(title__icontains=album_name)
            if albums.exists():
                return albums
            else:
                # Если альбом не найден, импортируем из Spotify
                result = import_album_from_spotify(album_name)
                if "successfully" in result.lower():
                    # Обновляем queryset с новым альбомом
                    return Album.objects.filter(title__icontains=album_name)
        return super().get_queryset()


class AlbumRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer




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