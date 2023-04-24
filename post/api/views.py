from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.mixins import DestroyModelMixin

from post.api.paginations import PostPagination
from post.api.permissions import IsOwner
from post.api.serializers import PostSerializer, PostDetailSerializer, PostUpdateCreateSerializer, PostCreateSerializer
from post.models import Post


class PostAPIView(ListAPIView):
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    pagination_class = PostPagination

    def get_queryset(self):
        queryset = Post.objects.filter(draft=False)
        return queryset


class PostAPICreateView(CreateAPIView):
    serializer_class = PostCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, modified_by=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = "slug"


class PostUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    serializer_class = PostUpdateCreateSerializer
    queryset = Post.objects.all()
    lookup_field = "slug"
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
