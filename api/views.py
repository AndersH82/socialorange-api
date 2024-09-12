from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout

@api_view(['POST'])
def token_refresh_view(request):
    refresh_token = request.data.get('refresh')

    if not refresh_token:
        raise ValidationError("Refresh token is required")

    try:
        RefreshToken.for_jwt_refresh_token(refresh_token)
        # Delete the refresh token from the database
        RefreshToken.blacklist(refresh_token)
    except Exception as e:
        return Response({'error': f"Failed to invalidate refresh token: {str(e)}"}, status=400)

    return Response({"message": "Refresh token invalidated"})

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my API for SocialOrange webpage!"
    })

@api_view(['GET'])
def clear_cookies_view(request):
    response = HttpResponse(status=204)
    response.delete_cookie(settings.JWT_AUTH_COOKIE, path='/')
    response.delete_cookie(settings.JWT_AUTH_REFRESH_COOKIE, path='/')
    return response

def logout_route(request):
    logout(request)
    return redirect('/')