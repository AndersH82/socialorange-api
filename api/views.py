from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE,
    JWT_AUTH_REFRESH_COOKIE,
    JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my API for SocialOrange webpage!"
    })


@api_view(['POST'])
def logout_route(request):
    # Get the refresh token from the request
    refresh_token = request.data.get('refresh')
    
    # Invalidate the refresh token
    try:
        RefreshToken.for_jwt_refresh_token(refresh_token)
        # Delete the refresh token from the database
        RefreshToken.blacklist(refresh_token)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
    
    # Clear cookies
    response = Response()
    response.delete_cookie(JWT_AUTH_COOKIE, path='/')
    response.delete_cookie(JWT_AUTH_REFRESH_COOKIE, path='/')
    
    return response