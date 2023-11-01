from http import HTTPStatus
<<<<<<< HEAD

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
=======

from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from api.filters import TitleFilter
from api.mixins import CreateDeleteViewSet
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
from api.permissions import (IsAdmin, IsAdminOrReadOnly,
                             IsAuthorModeratorAdminOrReadOnly)
from api.serializers import (CategorySerializer, CommentSerializer,
                             GenreSerializer, ReviewSerializer,
                             TitleReadSerializer, TitleSerializer,
<<<<<<< HEAD
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
=======
                             TokenSerializer, UserEditSerializer,
                             UserRegistrationSerializer, UserSerializer)
from api.utils import send_confirmation_code
from reviews.models import Category, Genre, Review, Title, User


class UserViewSet(viewsets.ModelViewSet):
    """Класс для управления User (пользователь)."""

    http_methods = ('get', 'patch', 'delete', 'post')
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
        serializer = self.get_serializer(
            user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update(request, *args, **kwargs)


class GenreViewSet(CreateDeleteViewSet):
    """Класс для управления Genre (жанры)."""

    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',)
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)


class CategoryViewSet(CreateDeleteViewSet):
    """Класс для управления Category (категории)."""

    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',)
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)


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
        return super().update(request, *args, kwargs)


class ReviewViewSet(viewsets.ModelViewSet):
    """Класс для управления Review (отзыв)."""

    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorModeratorAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get_title_object(self):
        return get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )

    def get_queryset(self):
        return self.get_title_object().reviews.all()

    def perform_create(self, serializer):
        author = self.request.user

        if self.get_title_object().reviews.filter(author=author).exists():
            raise ValidationError(
                "Можно оставить только один отзыв на проивезедение."
            )
        serializer.save(author=author, title=self.get_title_object())

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

    def get_rewiew_object(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        return get_object_or_404(
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
            Review,
            id=review_id,
            title_id=title_id
        )
<<<<<<< HEAD
        return review

    def get_queryset(self):
        return self.get_review().comments.all()
=======

    def get_queryset(self):
        return self.get_rewiew_object().comments.all()
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
<<<<<<< HEAD
            review=self.get_review()
        )

=======
            review=self.get_rewiew_object()
        )

    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update(request, *args, **kwargs)

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed

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
<<<<<<< HEAD
    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
=======
    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
