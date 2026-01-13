from django.urls import path

from . import views

urlpatterns = [
    # GET requests for data gathering
    path('users/get/', views.get_users_data),
    path('users/get/<int:pk>/', views.GetUserDataById.as_view()),
    path('posts/get/', views.get_posts_data),
    path('posts/get/<int:pk>/', views.GetPostDataById.as_view()),
    path('likes/get/', views.get_likes_data),
    path('likes/get/<int:pk>/', views.GetLikeDataById.as_view()),
    path('comments/get/', views.get_comments_data),
    path('follows/get/', views.get_follows_data),

    # PATCH requests for data update
    path('users/patch/username/<int:pk>/', views.EditUserName.as_view()),
    path('users/patch/image/<int:pk>/', views.EditUserImage.as_view()),
    path('users/patch/bio/<int:pk>/', views.EditUserBio.as_view()),
    path('users/patch/password/<int:pk>/', views.EditUserPassword.as_view()),

    # POST requests for data creation
    path('users/create/', views.create_user),
    path('posts/create/', views.create_post),
    path('likes/create/', views.create_like),
    path('comments/create/', views.create_comment),
    path('follows/create/', views.create_follow),

    # DELETE requests for specific data
    path('users/delete/<int:pk>/', views.delete_user),
    path('posts/delete/<int:pk>/', views.delete_post),
    path('likes/delete/<int:pk>/', views.delete_like),
    path('comments/delete/<int:pk>/', views.delete_comment),
    path('follows/delete/<int:pk>/', views.delete_follow),
]