from functools import partial

from django.contrib.admin.utils import lookup_field
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from .serializers import *

@api_view(['GET'])
@permission_classes([AllowAny])
def ping_server(request):
    return Response({"status": "ok"}, status=status.HTTP_200_OK)

# GET requests for data

@api_view(['GET'])
def get_users_data(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True, read_only=True)
    return Response(serializer.data)

class GetUserDataById(RetrieveAPIView):
    # GET request for a specific user
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

# Will test the new function, if ok, will remove this
#class UserLogin(APIView):
    #def post(self, request):
        #serializer = UserLoginSerializer(data=request.data)
        #if serializer.is_valid():
        #    email = serializer.validated_data['email']
        #    password = serializer.validated_data['password']
        #
        #   try:
        #       user = User.objects.filter(email=email, password=password).first()
        #       user_serializer = UserSerializer(user)
        #
        #       return Response(user_serializer.data, status=status.HTTP_200_OK)
        #   except User.DoesNotExist:
        #       return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

# new function | test
class UserLogin(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data["email"].strip().lower()
        password = serializer.validated_data["password"].strip()

        try:
            user = User.objects.get(email=email, password=password)
        except User.DoesNotExist:
            return Response(
                {"error": "Invalid email or password"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_posts_data(request):
    # error in this function
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

class GetPostDataById(RetrieveAPIView):
    # GET request for a specific Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'

@api_view(['GET'])
def get_likes_data(request):
    likes = Like.objects.all()
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)

class GetLikeDataById(RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    lookup_field = 'pk'

@api_view(['GET'])
def get_comments_data(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True, read_only=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_follows_data(request):
    follows = Follow.objects.all()
    serializer = FollowSerializer(follows, many=True, read_only=True)
    return Response(serializer.data)

# PATCH requests for data edit

class EditUserName(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangeUsernameSerializer
    lookup_field = 'pk'
    http_method_names = ['get', 'put', 'patch', 'options']

class EditUserImage(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangeImageSerializer
    lookup_field = 'pk'
    http_method_names = ['get', 'put', 'patch', 'options']

class EditUserBio(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangeBioSerializer
    lookup_field = 'pk'
    http_method_names = ['get', 'put', 'patch', 'options']

class EditUserPassword(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    lookup_field = 'pk'
    http_method_names = ['get', 'put', 'patch', 'options']

# POST requests for data creation

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def create_like(request):
    serializer = LikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=HTTP_201_CREATED)

@api_view(['POST'])
def create_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def create_follow(request):
    serializer = FollowSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# DELETE requests

@api_view(['DELETE', 'GET'])
def delete_user(request, pk=None):
    queryset = User.objects.all().filter(pk=pk)
    user = queryset[0]
    user.delete()
    return Response("User deleted", status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE', 'GET'])
def delete_post(request, pk=None):
    queryset = Post.objects.all().filter(pk=pk)
    post = queryset[0]
    post.delete()
    return Response("Post deleted", status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE', 'GET'])
def delete_like(request, pk=None):
    queryset = Like.objects.all().filter(pk=pk)
    like = queryset[0]
    like.delete()
    return Response("Like deleted", status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE', 'GET'])
def delete_comment(request, pk=None):
    queryset = Comment.objects.all().filter(pk=pk)
    comment = queryset[0]
    comment.delete()
    return Response("Comment deleted", status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE', 'GET'])
def delete_follow(request, pk=None):
    queryset = Follow.objects.all().filter(pk=pk)
    follow = queryset[0]
    follow.delete()
    return Response("Follow deleted", status=status.HTTP_204_NO_CONTENT)