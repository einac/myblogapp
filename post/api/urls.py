from django.urls import path
from post.api.views import PostAPIView, PostDetailAPIView, PostAPICreateView, PostUpdateAPIView

urlpatterns = [
    path("list/", PostAPIView.as_view(), name="list"),
    path("detail/<slug>", PostDetailAPIView.as_view(), name="detail"),
    path("create/", PostAPICreateView.as_view(), name="create"),
    path("update/<slug>", PostUpdateAPIView.as_view(), name="update"),

]
