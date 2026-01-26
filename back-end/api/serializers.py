from dataclasses import fields

from rest_framework import serializers
from core.models import *
from drf_extra_fields.fields import Base64ImageField
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ChangeUsernameSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username']

class ChangeBioSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['bio']

class ChangeImageSerializer(serializers.ModelSerializer):
    image = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['image']

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['password']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"