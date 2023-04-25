from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from favourite.api.paginations import FavouritePagination
from favourite.api.permissions import IsOwner
from favourite.api.paginations import FavouritePagination
from favourite.api.serializers import (
    FavouriteListSerializer,
    FavouriteCreateSerializer,
    FavouriteUpdateSerializer,
    FavouriteDeleteSerializer,
)
from favourite.models import Favourite


class FavouriteListAPIView(ListAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteListSerializer
    pagination_class = FavouritePagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)


class FavouriteCreateAPIView(CreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save(user=self.request.user)


class FavouriteUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteUpdateSerializer
    lookup_field = "pk"
    permission_classes = [IsOwner]


class FavouriteDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteDeleteSerializer
    lookup_field = "pk"
    permission_classes = [IsOwner]
