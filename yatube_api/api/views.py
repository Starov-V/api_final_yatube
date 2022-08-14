from django.shortcuts import get_object_or_404
from rest_framework import viewsets, exceptions, filters, permissions
from posts.models import Post, Group
from api.serializers import (PostSerializer,
                             GroupSerializer,
                             CommentSerializer,
                             FollowSerializer)
from rest_framework.pagination import LimitOffsetPagination
from api.permissions import AuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для обработки постов."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Функция для создания постов."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для просмотра групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для обработки постов."""

    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """Функция для отображения комментариев."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        """Функция для создания комментариев."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

    def perform_destroy(self, instance):
        """Функция для удаления комментариев."""
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Удаление чужого контента запрещено!'
            )
        instance.delete()

    def perform_update(self, serializer):
        """Функция для изменения комментариев."""
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!'
            )
        super(CommentViewSet, self).perform_update(serializer)


class FollowViewSet(viewsets.ModelViewSet):
    """ViewSet для подписок."""

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Функция для создания подписки."""
        if serializer.is_valid():
            serializer.save(
                user=self.request.user,
                following=serializer.validated_data['following']
            )

    def get_queryset(self):
        """Функция для отображения подписок."""
        queryset = self.request.user.follower.all()
        return queryset
