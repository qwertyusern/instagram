from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
schema_view = get_schema_view(
   openapi.Info(
      title="Spotify Api",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact("Xojiakbar Goipov. Email:<xojiakbargoipov3@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

from app1.views import *
from userapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',schema_view.with_ui('swagger', cache_timeout=0), name='swagger-doc'),
    path('users/', UserQosh.as_view()),
    path('user/<int:pk>/', UserGetUpdateDelete.as_view()),
    path('profils/', Profils.as_view()),
    path('profil/<int:pk>/', ProfilGet.as_view()),
    path('connections/', Connections.as_view()),
    path('connection/<int:pk>/', ConnectionDelete.as_view()),
    path('posts/', Posts.as_view()),
    path('medias/', Medias.as_view()),
    path('media/<int:pk>/', MediaGet.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

