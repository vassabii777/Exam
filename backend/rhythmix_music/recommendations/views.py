from rest_framework.views             import APIView
from rest_framework.permissions       import IsAuthenticated
from rest_framework.response          import Response
from tracks.serializers               import TrackSerializer
from services.recommendation_service  import get_track_recommendations


class RecommendedTracksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id

        recommend_tracks = get_track_recommendations(user_id)
        serializer = TrackSerializer(recommend_tracks, many=True)
        return Response(serializer.data)