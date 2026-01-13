from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    bio = models.CharField(default="", max_length=120)
    image = models.CharField(default="", blank=True, null=False)

class Post(models.Model):
    author_id = models.IntegerField(null=False, blank=False)
    author = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(max_length=2000, null=False, blank=False)
    likes = models.IntegerField(default=0, null=False, blank=False)

class Like(models.Model):
    post_id = models.IntegerField(null=False, blank=False)
    user_id = models.IntegerField(null=False, blank=False)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
    author_id = models.IntegerField(null=False, blank=False)
    author = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(max_length=1500, null=False, blank=False)

class Follow(models.Model):
    user_id = models.IntegerField(null=False, blank=False)
    following_id = models.IntegerField(null=False, blank=False)