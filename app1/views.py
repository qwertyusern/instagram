from django.shortcuts import render
from rest_framework import status, generics
from .serializers import *
from rest_framework.response import Response

class Posts(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSer

class Medias(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSer

class MediaGet(generics.RetrieveAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSer