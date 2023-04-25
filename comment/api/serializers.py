from django.contrib.auth.models import User
from rest_framework import serializers
from comment.models import Comment
from post.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title',)


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    user = UserSerializer()
    post = PostCommentSerializer()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self, obj):
        if obj.any_children:
            return CommentSerializer(obj.children(), many=True).data


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created', ]

    def validate(self, attrs):
        if attrs['parent']:
            if not attrs['parent'].post == attrs['post']:
                raise serializers.ValidationError("Birşeyler ters gitti!")

        return attrs


class CommentUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
