from django.urls import path
from post.api.views import PostAPIView, PostDetailAPIView, PostCreateAPIView, PostUpdateAPIView, PostDeleteAPIView

urlpatterns = [
    path("list/", PostAPIView.as_view(), name="list"),
    path("detail/<slug>", PostDetailAPIView.as_view(), name="detail"),
    path("create/", PostCreateAPIView.as_view(), name="create"),
    path("update/<slug>", PostUpdateAPIView.as_view(), name="update"),
    path("delete/<slug>", PostDeleteAPIView.as_view(), name="delete"),

]
