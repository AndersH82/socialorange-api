from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import root_route, logout_route
from django.conf import settings
from django.conf.urls.static import static


from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from .views import root_route, logout_route
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/login/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('profiles/', include('profiles.urls')),
    path('posts/', include('posts.urls')),
    path('comments/', include('comments.urls')),
    path('likes/', include('likes.urls')),
    path('followers/', include('followers.urls')),
    path('', root_route),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
