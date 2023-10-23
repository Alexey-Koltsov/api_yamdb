from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_simplejwt.tokens import RefreshToken


from api.permissions import IsAdmin
from api.serializers import (GenreSerializer,
                             CategorySerializer,
                             TitleSerializer,
                             TokenSerializer,
                             UserSerializer,
                             UserCreateListByAdminSerializer,
                             ReviewSerializer,
                             CommentSerializer,)

# ProfileGetUpdateDeleteByAdmin, UserMeGetUpdate,

from reviews.models import Genre, Category, Title, Review, Comment

User = get_user_model()


class UserCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Регистрация нового пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]

    def perform_create(self, serializer):
        username = serializer.validated_data['username']
        confirmation_code = get_random_string(length=16)
        serializer.save(
            confirmation_code=confirmation_code,
        )
        send_mail(
            subject='Код подтверждения для Yamdb',
            message=(f'"username": "{username}",'
                     f'"confirmation_code": "{confirmation_code}"'),
            from_email='yamdb@yandex.ru',
            recipient_list=[serializer.data['email']],
        )

    def create(self, request, *args, **kwargs):
        if 'username' in request.data.keys() and 'email' in request.data.keys():
            username = request.data['username']
            email = request.data['email']
            username_list = list(User.objects.all().values_list('username', flat=True))
            if username in username_list:
                user = get_object_or_404(User, username=username)
                if email != user.email:
                    return Response({'detail': 'Некорректный email.'},
                                    status=status.HTTP_400_BAD_REQUEST
                                    )
                serializer = self.get_serializer(user, data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(
                           serializer.data,
                           status=status.HTTP_200_OK,
                           headers=headers
                           )
        serializer = self.get_serializer(data=request.data)
        """if '' in request.data.values():
            return Response({'detail': 'Отсутствуют данные в запросе.'},
                            status=status.HTTP_400_BAD_REQUEST
                            )"""
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
            headers=headers
        )


class TokenCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Регистрация нового пользователя."""

    serializer_class = TokenSerializer
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, username=request.data['username'])
        if user['confirmation_code'] != request.data['confirmation_code']:
            return Response({'detail': 'Некорректный confirmation_code.'},
                            status=status.HTTP_400_BAD_REQUEST
                            )
        refresh = RefreshToken.for_user(user)
        data = {'token': str(refresh.access_token)}
        headers = self.get_success_headers(serializer.data)
        return Response(data,
                        status=status.HTTP_200_OK,
                        headers=headers
                        )


class UserCreateList(mixins.CreateModelMixin,
                     mixins.ListModelMixin, viewsets.GenericViewSet):
    """Cоздание пользователя и получение списка пользователей Админом."""

    queryset = User.objects.all()
    serializer_class = UserCreateListByAdminSerializer
    permission_classes = [IsAdmin,]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)


"""class ProfileRetrieveUpdateDestroy(viewsets.RetrieveUpdateDestroyAPIView):
    

    queryset = User.objects.all()
    serializer_class = ProfileGetUpdateDeleteByAdmin
    permission_classes = [IsAdmin,]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object(username=self.kwargs['username'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()"""


"""class UserMeRetrieveUpdate(viewsets.RetrieveUpdateAPIView):
    

    queryset = User.objects.all()
    serializer_class = ProfileGetUpdateDeleteByAdmin
    permission_classes = [IsAdmin,]"""


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdmin,]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]
    search_fields = ['name']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin,]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]
    search_fields = ['name']


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAdmin,]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]
    filterset_fields = {
        'category__slug': ['exact'],
        'genre__slug': ['exact'],
        'name': ['icontains'],
        'year': ['exact']
    }


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        review_id = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        new_queryset = Comment.objects.filter(review=review_id)
        return new_queryset

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
