from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class ProfilSer(serializers.ModelSerializer):
    class Meta:
        model=Profil
        fields="__all__"

class ConnectionSer(serializers.ModelSerializer):
    follower=ProfilSer
    following=ProfilSer
    class Meta:
        model=Connection
        fields="__all__"

class PostSer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"

class MediaSer(serializers.ModelSerializer):
    class Meta:
        model=Media
        fields="__all__"

class LikeSer(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields="__all__"

class CommentSer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"

class Comment_likeSer(serializers.ModelSerializer):
    class Meta:
        model=Comment_like
        fields="__all__"

class XabarSer(serializers.ModelSerializer):
    class Meta:
        model=Xabar
        fields="__all__"

class Reaksiya_xabarSer(serializers.ModelSerializer):
    class Meta:
        model=Reaksiya_xabar
        fields="__all__"

class UserSer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"