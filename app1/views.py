from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status, generics, filters
from .serializers import *

class UserQosh(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer

class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer


class ProfilQosh(generics.ListCreateAPIView):
    queryset=Profil.objects.all()
    serializer_class = ProfilSer

class ProfilUpdate(generics.UpdateAPIView):
    queryset=User.objects.all()
    serializer_class = ProfilSer