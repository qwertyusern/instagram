from django.shortcuts import render
from rest_framework import status, generics
from .serializers import *
from rest_framework.response import Response

class Posts(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSer

class PostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSer
    def perform_update(self, serializer):
        p=Profil.objects.get(user=self.request.user)
        q=Post.objects.filter(profile=p)
        if serializer.q is True:
            serializer.update()
        return Response(serializer)
    def perform_destroy(self, instance):
        p1=Profil.objects.get(username=self.request.user)
        q = Post.objects.filter(profile=p1)
        if q is True:
            instance.delete()
        return Response(instance)

class Medias(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSer


class MediaGet(generics.RetrieveAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSer