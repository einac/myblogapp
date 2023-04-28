from django.urls import path
from account.api.views import ProfileAPIView, UpdatePasswordViewAPIView, RegisterAPIView

app_name = "account"

urlpatterns = [
    path("me", ProfileAPIView.as_view(), name="me"),
    path("change-password", UpdatePasswordViewAPIView.as_view(), name="change-password"),
    path("register", RegisterAPIView.as_view(), name="register"),
]
