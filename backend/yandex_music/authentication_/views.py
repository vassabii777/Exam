from django.shortcuts import redirect
from .renderes import UserJSONRenderer

from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from .serializers import (
    RegistrationSerializer,
      LoginSerializer,
      UserSerializer
    )

from django.conf import settings
import urllib.parse
import requests
from django.http import JsonResponse


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def google_login(request):
    google_auth_url = "https://accounts.google.com/o/oauth2/v2/auth"

    params = {
        "client_id": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        "redirect_uri": "http://127.0.0.1:8000/api/v1/google/callback/",  
        "response_type": "code",
        "scope": "email profile",
        "access_type": "offline",
        "prompt": "consent",
    }

    url = f"{google_auth_url}?{urllib.parse.urlencode(params)}"

    return redirect(url)

@csrf_exempt
def google_callback(request):
    code = request.GET.get('code')

    if not code:
        return JsonResponse({"error": "Authorization code not provided"}, status=400)
    
    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        "code": code,
        "client_id": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        "client_secret": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
        "redirect_uri": "http://127.0.0.1:8000/api/v1/google/callback/",
        "grant_type": "authorization_code",
    }


    token_response = requests.post(token_url, data=token_data)

    if token_response.status_code == 200:
        token_json = token_response.json()
        return JsonResponse(token_json)
    else:

        return JsonResponse(token_response.json(), status=token_response.status_code)



class RegistrationAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserRetriveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = self.serializer_class(
            request.user, data=serializer_data, patrial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    