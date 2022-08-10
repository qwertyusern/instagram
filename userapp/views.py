from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, filters

from app1.serializers import UserSer,ProfilSer,ConnectionSer
from app1.models import Profil,Connection
from rest_framework.response import Response


class UserQosh(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer

class UserGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer

class Profils(generics.ListCreateAPIView):
    queryset=Profil.objects.all()
    serializer_class = ProfilSer
    filter_backends = [filters.SearchFilter]
    search_fields = ["ism"]

class ProfilGet(generics.RetrieveUpdateDestroyAPIView):
    queryset=Profil.objects.all()
    serializer_class = ProfilSer

class Connections(generics.ListCreateAPIView):
    queryset=Connection.objects.all()
    serializer_class = ConnectionSer
    def get_queryset(self):
        queryset = []
        ism = self.request.query_params.get('follower_ism')
        if ism is not None:
            p1 = Profil.objects.get(username=ism)
            queryset = Connection.objects.filter(follower_id=p1)
        f_ism = self.request.query_params.get('following_ism')
        if f_ism is not None:
            p1 = Profil.objects.get(username=f_ism)
            queryset = Connection.objects.filter(following_id=p1)
        return queryset



class ConnectionDelete(generics.DestroyAPIView):
    queryset=Connection.objects.all()
    serializer_class = ConnectionSer
    def perform_destroy(self, instance):
        p1=Profil.objects.get(username=self.request.user)
        if instance.following_id==p1 or instance.follower_id==p1:
            instance.delete()
        return Response(instance)
