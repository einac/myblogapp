from rest_framework import serializers
from favourite.models import Favourite
from post.models import Post


class FavouriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = "__all__"


class FavouriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('post', 'user', 'content',)

    def validate(self, attrs):
        print(attrs)
        queryset = Favourite.objects.filter(post=attrs['post'], user=attrs['user'])
        if queryset.exists():
            raise serializers.ValidationError("Bu post hali hazırda favorilerinizde ekli!")
        return attrs


class FavouriteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('content',)


class FavouriteDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('id', 'user', 'post', 'content',)
