from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_route),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('comments/', include('comments.urls')),
    path('followers/', include('followers.urls')),
    path('likes/', include('likes.urls')),
    path('posts/', include('posts.urls')),
    path('profiles/', include('profiles.urls')),
]
