from django.urls import path
from . import views

urlpatterns = [
    path('friendships/', views.FriendshipList.as_view(), name='friendship-list'),
    path('friendship/<int:pk>/', views.FriendshipDetail.as_view(), name='friendship-detail'),
]
