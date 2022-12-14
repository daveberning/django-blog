from django.urls import path, include
from blogging.views import PostListView, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name="blog_index"),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name="blog_detail"),
]