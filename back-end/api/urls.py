from django.urls import path

from . import views

urlpatterns = [
    # GET requests for data gathering
    path('users/get', views.get_users_data),
    path('users/get/<int:pk>/', views.GetUserDataById.as_view()),
    path('posts/get', views.get_posts_data),
    path('posts/get/<int:pk>/', views.GetPostDataById.as_view()),
    path('comments/get/', views.get_comments_data),
    path('follows/get/', views.get_follows_data),

    # POST requests for data creation
    path('users/create/', views.create_user),
    path('posts/create/', views.create_post),
    path('comments/create/', views.create_comment),
    path('follows/create/', views.create_follow),

    # DELETE requests for specific data
    path('users/delete/<int:pk>/', views.delete_user),
    path('posts/delete/<int:pk>/', views.delete_post),
    path('comments/delete/<int:pk>/', views.delete_comment),
    path('follows/delete/<int:pk>/', views.delete_follow),
]