from django.urls import path
from .views import ArtistListCreateView, ArtistRetrieveUpdateDestroyView, SpotifyImportArtistView


urlpatterns = [
    
    path('artists/', ArtistListCreateView.as_view(), name='artist-list-create'),
    path('artists/<uuid:pk>/', ArtistRetrieveUpdateDestroyView.as_view(), name='artist-detail'),
    
    path('import-artist-spotify/', SpotifyImportArtistView.as_view(), name='import-artist-spotify'),


]