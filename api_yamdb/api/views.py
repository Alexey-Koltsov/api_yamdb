from http import HTTPStatus

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from reviews.models import Category, Genre, Review, Title, User
from api.filters import TitleFilter
from api.permissions import (IsAdmin, IsAdminOrReadOnly,
                             IsAuthorModeratorAdminOrReadOnly)
from api.serializers import (CategorySerializer, CommentSerializer,
                             GenreSerializer, ReviewSerializer,
                             TitleReadSerializer, TitleSerializer,
                             TokenSerializer, UserEditSerializer,
                             UserRegistrationSerializer, UserSerializer)
from api.mixins import ListCreateDestroyViewSet
from api_yamdb.settings import DEFAULT_FROM_EMAIL


class UserViewSet(viewsets.ModelViewSet):
    """Класс для управления User (пользователь)."""
    http_methods = ('get', 'patch', 'delete', 'post', 'put')
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'

    @action(
        methods=['get', 'patch'],
        serializer_class=UserEditSerializer,
        permission_classes=[permissions.IsAuthenticated],
        detail=False,
        url_path='me',
    )
    def user_profile(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PATCH':
            serializer = self.get_serializer(
                user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update(request, *args, **kwargs)


class GenreViewSet(viewsets.ModelViewSet):
    """Класс для управления Genre (жанры)."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_object(self):
        return get_object_or_404(Genre, slug=self.kwargs['pk'])

    def retrieve(self, request, *args, **kwargs):
        return Response({'datail': 'method GET not allowed'},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED
                        )

    def update(self, request, *args, **kwargs):
        return Response({'datail': 'method GET not allowed'},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED
                        )

    def destroy(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)


class CategoryViewSet(viewsets.ModelViewSet):
    """Класс для управления Category (категории)."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_object(self):
        return get_object_or_404(Category, slug=self.kwargs['pk'])

    def retrieve(self, request, *args, **kwargs):
        return Response({'datail': 'method GET not allowed'},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED
                        )

    def update(self, request, *args, **kwargs):
        return Response({'datail': 'method GET not allowed'},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED
                        )

    def destroy(self, request, *args, **kwargs):
        if request.user.is_admin or request.user.is_superuser:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)


class TitleViewSet(viewsets.ModelViewSet):
    """Класс для управления Title (произведение)."""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = TitleFilter
    search_fields = ['name', 'description']

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH', 'DELETE'):
            return TitleSerializer
        return TitleReadSerializer

    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        avg_rating = instance.reviews.aggregate(Avg('score'))['score__avg']
        if avg_rating is not None:
            serializer.data['rating'] = round(avg_rating, 2)
        else:
            serializer.data['rating'] = None
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    """Класс для управления Review (отзыв):
создание отзыва, изменение отзыва,
получение одного или списка отзывов,
удаление отзыва.
"""
    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorModeratorAdminOrReadOnly
    ]

    def get_review(self):
        title_id = self.kwargs.get('title_id')
        return get_object_or_404(Title, pk=title_id)
    
    def get_queryset(self):
        return self.get_review().reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_review())

    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    """Класс для управления Comment (комментарий)."""
    serializer_class = CommentSerializer
    permission_classes = [   
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorModeratorAdminOrReadOnly
    ]
    
    def get_review(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(
            Review,
            id=review_id,
            title_id=title_id
        )
        return review

    def get_queryset(self):
        return self.get_review().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            review=self.get_review()
        )

    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update(request, *args, **kwargs)


def send_confirmation_code(user: User):
    """Отправка кода подтверждения."""

    confirmation_code = default_token_generator.make_token(user)
    message = f'Ваш код подтверждения: {confirmation_code}'

    send_mail(
        'Ваш код подтверждения',
        message,
        DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def signup(request):
    """Регистрация нового пользователя."""

    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    email = serializer.validated_data.get('email')
    user, created = User.objects.get_or_create(
        username=username,
        email=email
    )
    send_confirmation_code(user)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_token(request):
    """Получение токена."""
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )
    if default_token_generator.check_token(
        user,
        serializer.validated_data['confirmation_code']
    ):
        token = AccessToken.for_user(user)
        return Response({'token': str(token)}, status=HTTPStatus.OK)
    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
