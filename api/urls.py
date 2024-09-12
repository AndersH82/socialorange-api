from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import token_refresh_view, root_route, clear_cookies_view, logout_route  # Import logout_route
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Root route
    path('', root_route),

    # REST Framework URLs
    path('api-auth/', include('rest_framework.urls')),

    # dj-rest-auth URLs
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/logout/', logout_route),  # Use the imported logout_route
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # Custom views
    path('dj-rest-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', clear_cookies_view, name='logout'),

    # Include other app URLs
    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('comments.urls')),
    path('', include('likes.urls')),
    path('', include('followers.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)