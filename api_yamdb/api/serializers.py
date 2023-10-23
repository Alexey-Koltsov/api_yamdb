import re

from django.contrib.auth import get_user_model
from rest_framework import serializers, validators
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


class TokenSerializer(serializers.ModelSerializer):
    """Сериализатор для создания токенов."""

    class Meta:
        model = User
        fields = ('username',)


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
