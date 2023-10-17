from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.permissions import IsAuthorOrReadOnly
from api.serializers import UserSerializer


User = get_user_model()


class UserCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Регистрация нового пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )
