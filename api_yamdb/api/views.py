from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from rest_framework import filters, permissions, mixins, viewsets

from api.permissions import IsAdmin
from api.serializers import UserSerializer, UserCreateListByAdminSerializer


User = get_user_model()


class UserCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Регистрация нового пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]

    def perform_create(self, serializer):
        confirmation_code = get_random_string(length=16)
        serializer.save(
            confirmation_code=confirmation_code,
        )
        send_mail(
            subject='Код подтверждения для Yamdb',
            message=f'"confirmation_code": "{confirmation_code}"',
            from_email='yamdb@yandex.ru',
            recipient_list=[serializer.data['email']],
        )


class UserCreateList(mixins.CreateModelMixin,
                     mixins.ListModelMixin, viewsets.GenericViewSet):
    """Cоздание пользователя и получение списка пользователей Админом."""

    queryset = User.objects.all()
    serializer_class = UserCreateListByAdminSerializer
    permission_classes = [IsAdmin,]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
