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
    path('rest-auth/logout/', logout_route),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('comments.urls')),
    path('', include('likes.urls')),
    path('', include('followers.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
