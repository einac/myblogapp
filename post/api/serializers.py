from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="detail",
        lookup_field="slug"
    )

    username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['username', 'url']

    def get_username(self, obj):
        return str(obj.user.username)


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'image', 'created', 'modified', 'modified_by']


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

