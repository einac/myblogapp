from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveDestroyAPIView,
                                     )
from post.api.paginations import PostPagination
from post.api.permissions import IsOwner
from post.api.serializers import PostSerializer, PostDetailSerializer, PostUpdateSerializer, PostCreateSerializer
from post.models import Post


class PostAPIView(ListAPIView):
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    pagination_class = PostPagination

    def get_queryset(self):
        queryset = Post.objects.filter(draft=False)
        return queryset


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, modified_by=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = "slug"


class PostUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PostUpdateSerializer
    queryset = Post.objects.all()
    lookup_field = "slug"
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class PostDeleteAPIView(RetrieveDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = "slug"
    permission_classes = [IsOwner]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
