from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)

class Post(models.Model):
    author_id = models.IntegerField(null=False, blank=False)
    author = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(max_length=2000, null=False, blank=False)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
    author_id = models.IntegerField(null=False, blank=False)
    author = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(max_length=1500, null=False, blank=False)

class Follow(models.Model):
    user_id = models.IntegerField(null=False, blank=False)
    following_id = models.IntegerField(null=False, blank=False)