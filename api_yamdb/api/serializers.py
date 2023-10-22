import re

from django.contrib.auth import get_user_model, models
from django.shortcuts import get_object_or_404
from rest_framework import serializers, validators, status
from rest_framework.response import Response
from rest_framework_simplejwt import exceptions
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.relations import SlugRelatedField
from reviews.models import Genre, Category, Title, Comment, Review

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для самостоятельной регистрации пользователей."""

    username = serializers.SlugField(
        max_length=150,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        max_length=254,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    confirmation_code = serializers.HiddenField(
        default='',
        write_only=True,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'confirmation_code')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" запрещено!'
            )
        if not re.match(r'^[\w.@+-]+\Z', value):
            raise serializers.ValidationError(
                'Имя пользователя должно соотвестсвовать паттерну!'
            )
        return value


class UserCreateListByAdminSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создание пользователя и
    получение списка пользователей Админом.
    """

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" запрещено!'
            )
        if not re.match(r'^[\w.@+-]+\Z', value):
            raise serializers.ValidationError(
                'Имя пользователя должно соответствовать паттерну!'
            )
        return value


"""class ProfileGetUpdateDeleteByAdmin(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" запрещено!'
            )
        if not re.match(r'^[\w.@+-]+\Z', value):
            raise serializers.ValidationError(
                'Имя пользователя должно соответствовать паттерну!'
            )
        return value"""


"""class UserMeGetUpdate(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" запрещено!'
            )
        if not re.match(r'^[\w.@+-]+\Z', value):
            raise serializers.ValidationError(
                'Имя пользователя должно соответствовать паттерну!'
            )
        return value"""


class ConfirmationCodeField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('style', {})

        kwargs['style']['input_type'] = 'confirmation_code'
        kwargs['write_only'] = True

        super().__init__(*args, **kwargs)


class CustomTokenObtainSerializer(TokenObtainSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField(write_only=True)
        self.fields['confirmation_code'] = ConfirmationCodeField()

    def validate(self, attrs):

        code_list = list(User.objects.all().values_list('confirmation_code', flat=True))

        self.user = get_object_or_404(
            User,
            username=attrs[self.username_field],
            confirmation_code=attrs['confirmation_code'],
        )

        if not attrs['confirmation_code'] in code_list:
            raise serializers.ValidationError(
                'Код подтверждения необходим!'
            )

        return {}


class CustomTokenObtainPairSerializer(CustomTokenObtainSerializer):
    token_class = RefreshToken

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()
        del self.fields['password']
        self.fields['confirmation_code'] = serializers.CharField()

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['token'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            models.update_last_login(None, self.user)

        return data


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('post', 'author')


class ReviewSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(read_only=True,
                            default=serializers.CurrentUserDefault(),
                            slug_field='username')
    review = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Review
