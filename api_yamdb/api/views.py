from http import HTTPStatus

from django.contrib.auth.tokens import default_token_generator
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from api.filters import TitleFilter
from api.mixins import GenreCategoryViewSetMixin, CreateDeleteViewSet, CustomUpdateMixin
from api.permissions import (IsAdmin, IsAdminOrReadOnly,
                             IsAuthorModeratorAdminOrReadOnly)
from api.serializers import (CategorySerializer, CommentSerializer,
                             GenreSerializer, ReviewSerializer,
                             TitleReadSerializer, TitleSerializer,
                             TokenSerializer,
                             UserRegistrationSerializer, UserSerializer)
from api.utils import send_confirmation_code
from reviews.models import Category, Genre, Review, Title, User


class UserViewSet(viewsets.ModelViewSet):
    """Класс для управления User (пользователь)."""

    http_method_names = ('get', 'patch', 'delete', 'post')
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'

    @action(
        methods=['get', 'patch'],
        serializer_class=UserSerializer,
        permission_classes=[permissions.IsAuthenticated],
        detail=False,
        url_path='me',
    )
    def user_profile(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(
            user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        if 'role' in request.data:
            return Response(
                {'detail': 'Изменение роли пользователя запрещено.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class GenreViewSet(GenreCategoryViewSetMixin, CreateDeleteViewSet):
    """Класс для управления Genre (жанры)."""

    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer


class CategoryViewSet(GenreCategoryViewSetMixin, CreateDeleteViewSet):
    """Класс для управления Category (категории)."""

    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class TitleViewSet(CustomUpdateMixin, viewsets.ModelViewSet):
    """Класс для управления Title (произведение)."""

    queryset = Title.objects.all().annotate(rating=Avg('reviews__score'))
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = TitleFilter
    search_fields = ['name', 'description']

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH', 'DELETE'):
            return TitleSerializer
        return TitleReadSerializer


class ReviewViewSet(viewsets.ModelViewSet, CustomUpdateMixin):
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


class CommentViewSet(viewsets.ModelViewSet, CustomUpdateMixin):
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


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def signup(request):
    """Регистрация нового пользователя."""

    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    email = serializer.validated_data.get('email')
    user, _ = User.objects.get_or_create(
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