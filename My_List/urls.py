from django.urls import path
from . import views
from .views import (PostCreateView, PostListView, PostUpdateView, PostDeleteView,
                   UserPostListView, PostDetailWithCommentView, CommentCreateView,
                   CommentDeleteView)
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_view'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user_post_view'),
    path('post/new/', views.PostCreateView.as_view(), name='create_view'),
    path('post/<int:pk>/', views.PostDetailWithCommentView.as_view(), name='Detail_view'),
    path('about/', views.about, name='my_list-about'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update_view'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_view'),
    path('post/<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment_create'),
    path('post/<int:pk>/comment/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]

