from rest_framework import generics
from .models        import Artist
from .serializers   import ArtistSerializer
from services.services       import import_artist_from_spotify

from rest_framework.response import Response
from rest_framework.views    import APIView



# ARTIST VIEWS
class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_queryset(self):
        # Если запрос содержит параметр поиска, ищем артиста по имени
        artist_name = self.request.query_params.get('search')
        if artist_name:
            # Пытаемся найти артиста в базе данных
            artists = Artist.objects.filter(name__icontains=artist_name)
            if artists.exists():
                return artists
            else:
                # Если артист не найден, импортируем из Spotify
                result = import_artist_from_spotify(artist_name)
                if "successfully" in result.lower():
                    # Обновляем queryset с новым артистом
                    return Artist.objects.filter(name__icontains=artist_name)
        return super().get_queryset()
    

class ArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    


# Импорт Артистов из spotify(вручную)
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
    
