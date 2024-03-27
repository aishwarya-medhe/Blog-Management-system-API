from django.urls import path
from .views import CommentListCreateView,CommentRetrieveUpdateDeleteView

urlpatterns=[
    path('posts/<int:post_id>/comments/',CommentListCreateView.as_view(),name='comment-list-create'),
    path('posts/<int:post_id>/comments/<int:comment_id>/',CommentRetrieveUpdateDeleteView.as_view(),name='comment-detail'),
]