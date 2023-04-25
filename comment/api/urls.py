from django.urls import path
from comment.api.views import CommentCreateAPIView, CommentAPIView, CommentUpdateAPIView, CommentDeleteAPIView

app_name = "comment"

urlpatterns = [
    path("create/", CommentCreateAPIView.as_view(), name="create"),
    path("list/", CommentAPIView.as_view(), name="list"),
    path("update/<pk>", CommentUpdateAPIView.as_view(), name="update"),
    path("delete/<pk>", CommentDeleteAPIView.as_view(), name="delete"),
]
