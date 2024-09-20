from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import jwt
import time
from datetime import timedelta

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my API for SocialOrange webpage!"
    })

@api_view(['POST'])
def logout_route(request):
    # Get the current access token
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return Response({"detail": "Authorization header missing"}, status=400)
    
    try:
        access_token = auth_header.split()[1]
    except IndexError:
        return Response({"detail": "Invalid Authorization header format"}, status=400)

    # Decode the access token
    try:
        decoded_token = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        # Token has expired, refresh it
        return Response({"detail": "Token has expired"}, status=401)
    except jwt.DecodeError:
        return Response({"detail": "Invalid access token"}, status=401)

    # Refresh the token
    refresh_token = decoded_token.get('refresh')
    if not refresh_token:
        return Response({"detail": "No refresh token found"}, status=400)

    try:
        # Decode the refresh token
        decoded_refresh_token = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=['HS256'])

        # Create new access and refresh tokens
        new_access_token = jwt.encode(
            {
                'exp': int(time.time()) + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds(),
                'iat': int(time.time()),
                'sub': decoded_refresh_token['sub'],
                'scope': decoded_refresh_token['scope']
            },
            settings.SECRET_KEY,
            algorithm='HS256'
        )

        new_refresh_token = jwt.encode(
            {
                'exp': int(time.time()) + settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds(),
                'iat': int(time.time()),
                'sub': decoded_refresh_token['sub'],
                'scope': decoded_refresh_token['scope']
            },
            settings.SECRET_KEY,
            algorithm='HS256'
        )

        # Update cookies
        response = Response({"detail": "Logged out successfully"})
        response.set_cookie(
            key=settings.JWT_AUTH_COOKIE,
            value=new_access_token,
            httponly=True,
            expires=int(time.time()) + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds(),
            max_age=0,
            samesite=settings.JWT_AUTH_SAMESITE,
            secure=settings.JWT_AUTH_SECURE,
        )
        response.set_cookie(
            key=settings.JWT_AUTH_REFRESH_COOKIE,
            value=new_refresh_token,
            httponly=True,
            expires=int(time.time()) + settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds(),
            max_age=0,
            samesite=settings.JWT_AUTH_SAMESITE,
            secure=settings.JWT_AUTH_SECURE,
        )
        return response

    except jwt.DecodeError:
        return Response({"detail": "Invalid refresh token"}, status=401)
    except Exception as e:
        return Response({"detail": str(e)}, status=500)