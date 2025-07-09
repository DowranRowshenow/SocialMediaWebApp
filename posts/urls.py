from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path('', login_required(views.PostsView.as_view()), name="posts"),
    path('<int:pk>/post_detail/', login_required(views.PostDetailView.as_view()), name="post_detail"),
    path('create_post/', login_required(views.CreatePostView.as_view()), name="create_post"),
    path('<int:pk>/edit_post/', login_required(views.EditPostView.as_view()), name="edit_post"),
    path('like_post/<post_id>/', login_required(views.LikePostView.as_view()), name="like_post"),
    path('dislike_post/<post_id>/', login_required(views.DislikePostView.as_view()), name="dislike_post"),
    path('<int:pk>/delete_post/', login_required(views.DeletePostView.as_view()), name="delete_post"),
    path('<int:post_id>/post_comment/', login_required(views.CommentPostView.as_view()), name="comment_post"),
]