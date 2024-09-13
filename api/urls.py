from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import root_route, logout_route
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path(r'ws://', include('profiles.urls')),
    path(r'ws://', include('posts.urls')),
    path(r'ws://', include('comments.urls')),
    path(r'ws://', include('likes.urls')),
    path(r'ws://', include('followers.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
