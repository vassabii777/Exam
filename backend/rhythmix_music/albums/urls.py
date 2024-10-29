from django.urls import path
from .views import AlbumListCreateView, AlbumRetrieveUpdateDestroyView, SpotifyImportAlbumView


urlpatterns = [
     # Album URLs
    path('albums/', AlbumListCreateView.as_view(), name='album-list-create'),
    path('albums/<uuid:pk>/', AlbumRetrieveUpdateDestroyView.as_view(), name='album-detail'),
    path('import-album-spotify/', SpotifyImportAlbumView.as_view(), name='import-album-spotify'),
]