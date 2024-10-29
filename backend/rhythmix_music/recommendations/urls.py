from django.urls import path

from .views      import RecommendedTracksView


urlpatterns = [
    # Эндпоинт для получения списка рекомендованных треков
    path('tracks/recommendations/', RecommendedTracksView.as_view(), name='recommended-tracks'),
]