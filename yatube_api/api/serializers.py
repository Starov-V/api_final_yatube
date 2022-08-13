from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from posts.models import Comment, Post, Group, Follow

class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для групп."""

    class Meta:
        """Мета-класс для сериализатора для групп."""

        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для постов."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        """Мета-класс для сериализатора для постов."""

        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        """Мета-класс для сериализатора комментариев."""
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для подписок."""
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset =get_user_model().objects.all()
    )
    class Meta:
        """Мета-класс для сериализатора для подписок."""
        fields = '__all__'
        read_only_fields = ('user', )
        model = Follow

    def validate(self, data):
        following = get_object_or_404(
            get_user_model(), username=data['following']
        )
        if self.context['request'].user == following or Follow.objects.filter(user=self.context['request'].user, following=following):
            raise serializers.ValidationError
        return data