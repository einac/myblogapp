from django.urls import path
from favourite.api.views import (
    FavouriteListAPIView,
    FavouriteCreateAPIView,
    FavouriteUpdateAPIView,
    FavouriteDeleteAPIView,
)

app_name = "favourite"

urlpatterns = [
    path("list/", FavouriteListAPIView.as_view(), name="list"),
    path("create/", FavouriteCreateAPIView.as_view(), name="create"),
    path("update/<pk>", FavouriteUpdateAPIView.as_view(), name="update"),
    path("delete/<pk>", FavouriteDeleteAPIView.as_view(), name="delete"),

]
